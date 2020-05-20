from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.toolbox.secretutil import SecretUtil
import json
import random

class Automorphic:
    def __init__(self, group):
        self.group = group

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
        return vk, sk

    def sign(self, pp, sk, m):
        sign={}
        return sign

    def verify(self, pp, vk, m, sign):
        return true

if __name__ == "__main__":
    group = PairingGroup('MNT159')
    autinst = Automorphic(group)
    pp = autinst.setup()