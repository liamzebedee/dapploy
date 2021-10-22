
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict
from . import Agent, NetworkedNode

class PeerMixin():
    def __init__(self):
        # super(PeerMixin, self).__init__()
        super().__init__()
        self.downloads = defaultdict(lambda: 0)
    
    def download(self, agent):
        self.downloads[agent] += 1

class Peer(Agent, NetworkedNode, PeerMixin):
    def __init__(self, ctx):
        super(PeerMixin, self).__init__()
        super().__init__('Peer')
    
    def step(self, i):
        pass
