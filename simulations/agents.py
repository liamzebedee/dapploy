
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict

class Agent(ABC):
    __metaclass__ = abc.ABCMeta
    agent_type = 'Agent'

    def __init__(self, type):
        super().__init__()
        self.agent_type = type
    
    def set_id(self, _id):
        self.id = _id

    @abstractmethod
    def step(self, i):
        pass

class NetworkedNode:
    def __init__(self):
        super().__init__()
        self.position = [random()]
    
    def distance_to(self, node):
        return math.dist(node.position, self.position)

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