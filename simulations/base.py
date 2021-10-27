
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict
from agents.user import *
from agents.load_balancer import *
from agents.peer import *


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
                agent.step(self.time)



# Protocol
# ----------------------------------

# class Token:
#     def __init__(self):
#         self.balances = defaultdict(lambda: 0)
    
#     def set_balance(self, id, amount):
#         self.balances[id] = amount
    
#     def transfer(self, from_, to, amount):
#         assert amount >= self.balances[from_]
#         self.balances[from_] -= amount
#         self.balances[to] += amount

class Protocol:
    def __init__(self):
        self.peers = []
        self.load_balancers = []
        self.staked = defaultdict(lambda: 0)
        
        # target bandwidth of 3MB / 1.5s.
        # 1mb : x ms
        # target_rate = 3.5 / 2.
        self.target_rtt = 250
    
    def report(self, agent, avgs, reqs_served, reqs_served_total):
        assert agent.id in list(map(lambda x: x.id, self.load_balancers))
        
        total_rewards = 1_000
        reward_per_requests_served = 1 / 500
        PEERS_SHARE = 0.8
        LOAD_BALANCERS_SHARE = 0.2
        # print(reqs_served)
        # print(reqs_served_total)

        for peer_id, avg_rtt in avgs.items():
            # mint rewards.
            if avg_rtt < self.target_rtt:
                reward = (reqs_served[peer_id] / reqs_served_total) * total_rewards * PEERS_SHARE
                self.staked[peer_id] += reward
        
        self.staked[agent.id] += max(reqs_served_total * reward_per_requests_served, LOAD_BALANCERS_SHARE * total_rewards)
    
    def stake(self, id_, amount):
        self.staked[id_] = amount
    
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
NUM_STEPS = 3000

# Setup protocol.
protocol = Protocol()

class Context:
    def __init__(self, simulation, protocol):
        self.simulation = simulation
        self.protocol = protocol

ctx = Context(simulation, protocol)

# End-users.
for i in range(0, 1_000):
    agent = User(ctx)
    simulation.add_agent(agent)

    protocol.stake(agent.id, 1)

# Load balancer nodes.
for i in range(0, 20):
    agent = LoadBalancer(ctx)
    simulation.add_agent(agent)

    protocol.stake(agent.id, 1_000_000)
    protocol.register_load_balancer(agent)

# Peer nodes.
for i in range(0, 100):
    agent = Peer(ctx)
    simulation.add_agent(agent)

    protocol.stake(agent.id, 100_000)
    protocol.register_peer(agent)


simulation.simulate(2500)

# for b in protocol.load_balancers:
#     print(len(b.peerset))

for agent in simulation.agents:
    staked = protocol.staked[agent.id]
    print("{:>7d} {} {}".format(agent.id, agent.agent_type, staked))