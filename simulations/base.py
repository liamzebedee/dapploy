
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict
from agents import Agent, User, Peer, LoadBalancer

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

# Setup protocol.
protocol = Protocol()

class Context:
    def __init__(self, protocol):
        self.protocol = protocol

ctx = Context(protocol)

# End-users.
for i in range(0, 1_000):
    agent = User(ctx)
    simulation.add_agent(agent)

# Load balancer nodes.
for i in range(0, 20):
    agent = LoadBalancer(ctx)
    simulation.add_agent(agent)

    protocol.register_load_balancer(agent)

# Peer nodes.
for i in range(0, 100):
    agent = Peer(ctx)
    simulation.add_agent(agent)

    protocol.register_peer(agent)

# for b in protocol.load_balancers:
#     print(len(b.peerset))

simulation.simulate(NUM_STEPS)
