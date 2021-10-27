
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict
from .agent import Agent
from .networked_node import NetworkedNode

class User(Agent, NetworkedNode):
    def __init__(self, ctx):
        super().__init__('User')
        self.ctx = ctx
        self.downloads = defaultdict(lambda: 0)
    
    def step(self, i):
        if random() < 0.60:
            return

        # Select a load balancer at random.
        balancer = self.ctx.protocol.request_balancer()
        
        # Select closest peer.
        # peer = balancer.find_closest_peer()
        resource = None
        signed_request = balancer.begin_request(self, resource)

        # Download.
        peer = signed_request.server
        peer.request(signed_request)

        # simulate RTT.
        rtt = 200
        # 80% of time

        # Report score and download speed to load balancer.
        balancer.end_request(signed_request.id, self, rtt)