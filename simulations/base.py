
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math

# 
# Agent-based simulation.
# 

# Agents.
# ----------------------------------

class Simulation:
    agent_id_counter = 0
    agents = []
    time = 0

    def add_agent(self, agent):
        self.agent_id_counter += 1
        agent.set_id(self.agent_id_counter)

        self.agents.append(agent)
    
    def simulate(self, ticks):
        for i in range(1, ticks):
            self.time += 1
            for agent in self.agents:
                agent.step(i)


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
        self.downloads = 0
    
    def download(self):
        self.downloads += 1

class Peer(Agent, NetworkedNode, PeerMixin):
    def __init__(self):
        super(PeerMixin, self).__init__()
        super().__init__('Peer')
    
    def step(self, i):
        pass

class LoadBalancer(Agent, NetworkedNode, PeerMixin):
    def __init__(self):
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
    def __init__(self):
        pass
    
    def step(self, i):
        # Select a load balancer at random.
        balancer = protocol.request_balancer()
        
        # Select closest peer.
        peer = balancer.find_closest_peer()

        # Download.
        peer.download()


# Protocol
# ----------------------------------

class Protocol:
    def __init__(self):
        self.peers = []
        self.load_balancers = []
    
    def register_peer(self, peer):
        self.peers.append(peer)

        added = False
        while not added:
            balancer = choice(self.load_balancers)
            added = balancer.on_register_peer(peer)
    
    def register_load_balancer(self, balancer):
        self.load_balancers.append(balancer)
    
    def request_balancer(self):
        # pick a random load balancer.
        return choice(self.load_balancers)
    


# Global state.
# ----------------------------------

simulation = Simulation()
NUM_STEPS = 10_000

# Setup.
protocol = Protocol()

for i in range(0, 1_000):
    agent = User()
    simulation.add_agent(agent)

for i in range(0, 20):
    agent = LoadBalancer()
    simulation.add_agent(agent)

    protocol.register_load_balancer(agent)

for i in range(0, 100):
    agent = Peer()
    simulation.add_agent(agent)

    protocol.register_peer(agent)

# for b in protocol.load_balancers:
#     print(len(b.peerset))

simulation.simulate(NUM_STEPS)
