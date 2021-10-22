
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict

class User(Agent, NetworkedNode):
    def __init__(self, ctx):
        super().__init__('User')
        self.ctx = ctx
    
    def step(self, i):
        # Select a load balancer at random.
        balancer = self.ctx.protocol.request_balancer()
        
        # Select closest peer.
        peer = balancer.find_closest_peer()

        # Download.
        peer.download(self)