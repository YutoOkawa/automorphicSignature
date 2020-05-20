from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.toolbox.secretutil import SecretUtil
import json
import random

class Automorphic:
    def __init__(self, group):
        self.group = group

    def changeMessageDH(self, pp, msg):
        messageDh = {}
        messageHash = self.group.hash(msg)
        messageDh['M'] = pp['G'] ** messageHash
        messageDh['N'] = pp['H'] ** messageHash
        return messageDh

    def setup(self):
        pp = {}
        pp['G'] = self.group.random(G1)
        pp['H'] = self.group.random(G2)
        pp['F'] = self.group.random(G1)
        pp['K'] = self.group.random(G1)
        pp['T'] = self.group.random(G1)
        return pp

    def keygen(self, pp):
        vk = {}
        x = group.random(ZR)
        sk = x
        vk['X'] = pp['G'] ** x
        vk['Y'] = pp['H'] ** x
        return vk, sk

    def sign(self, pp, sk, message):
        sign = {}
        messageDh = self.changeMessageDH(pp, message)
        c, r = self.group.random(ZR), self.group.random(ZR)
        sign['A'] = (pp['K'] * (pp['T'] ** r) * messageDh['M']) ** (1 / (sk + c))
        sign['C'] = pp['F'] ** c
        sign['D'] = pp['H'] ** c
        sign['R'] = pp['G'] ** r
        sign['S'] = pp['H'] ** r
        return sign

    def verify(self, pp, vk, message, sign):
        messageDh = self.changeMessageDH(pp, message)
        pairCH = pair(sign['C'], pp['H'])
        pairFD = pair(pp['F'], sign['D'])
        if pairCH != pairFD:
            print('e(C,H) != e(F,D)')
            return False
        else:
            print('e(C,H) == e(F,D)')

        pairRH = pair(sign['R'], pp['H'])
        pairGS = pair(pp['G'], sign['S'])
        if pairRH != pairGS:
            print('e(R,H) != e(G,S)')
            return False
        else:
            print('e(R,H) == e(G,S)')

        pairAYD = pair(sig['A'], vk['Y'] * sign['D'])
        pairKMH = pair(pp['K'] * messageDh['M'], pp['H'])
        pairTS = pair(pp['T'], sig['S'])
        if pairAYD != pairKMH * pairTS:
            print('e(A,Y*D) != e(K*M,H) * e(T,S)')
            return False

        print('e(A,Y*D) == e(K*M,H) * e(T,S)')

        return True

if __name__ == "__main__":
    group = PairingGroup('MNT159')
    autinst = Automorphic(group)
    pp = autinst.setup()
    print(pp)
    vk, sk = autinst.keygen(pp)
    print(vk)
    print(sk)
    sig = autinst.sign(pp, sk, 'hello world')
    print(sig)
    print(autinst.verify(pp, vk, 'hello world', sig))