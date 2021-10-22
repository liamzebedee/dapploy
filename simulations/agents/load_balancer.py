
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict

class LoadBalancer(Agent, NetworkedNode, PeerMixin):
    def __init__(self, ctx):
        super().__init__('LoadBalancer')
        self.peerset = []
    
    def step(self, i):
        pass
    
    def on_register_peer(self, peer):
        DISTANCE_THRESHOLD = 0.2
        if self.distance_to(peer) < DISTANCE_THRESHOLD:
            self.peerset.append(peer)
            return True
        return False
    
    def find_closest_peer(self):
        # choose random peer
        # TODO: keep track of peer performance, and choose
        # peer with best score
        if len(self.peerset) > 0:
            return choice(self.peerset)
        return self