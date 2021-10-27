
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict
import copy
from .agent import Agent
from .networked_node import NetworkedNode

class PeerMixin():
    def __init__(self):
        # super(PeerMixin, self).__init__()
        super().__init__()
        self.downloads = defaultdict(lambda: 0)
        self.uploads = defaultdict(lambda: 0)
        self.requests = {}
        # self.total_upload = 0
        # self.total_download = 0
    
    def request(self, signed_request):
        # verify signature of request obj, comes from load balancer.
        self.requests[signed_request.id] = copy.copy(signed_request)
        assert signed_request.server.id == self.id

        # simulate rtt.
        rtt = 201

        content_size = 1
        self.uploads[signed_request.client] += content_size

        # end request and report rtt to load balancer.
        signed_request.load_balancer.end_request(signed_request.id, self, rtt)


class Peer(Agent, NetworkedNode, PeerMixin):
    def __init__(self, ctx):
        super(PeerMixin, self).__init__()
        super().__init__('Peer')
    
    def step(self, i):
        pass
