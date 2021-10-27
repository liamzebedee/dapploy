
import abc
from abc import ABC, abstractmethod
from random import random, choice
import math
from collections import defaultdict, namedtuple
import functools
from .agent import Agent
from .networked_node import NetworkedNode
from .peer import PeerMixin

class Request:
    def __init__(self, id_, timestamp, client, server, load_balancer, content, client_reported_rtt, server_reported_rtt):
        self.id = id_
        self.timestamp = timestamp
        self.client = client
        self.server = server
        self.load_balancer = load_balancer
        self.content = content
        self.client_reported_rtt = client_reported_rtt
        self.server_reported_rtt = server_reported_rtt

REPORTING_INTERVAL = 40

class LoadBalancer(Agent, NetworkedNode, PeerMixin):
    def __init__(self, ctx):
        super().__init__('LoadBalancer')
        self.peerset = []
        self.requests_served = 0
        self.requests = {}
        self.ctx = ctx
    
    def step(self, i):
        if i % REPORTING_INTERVAL == 0:
            self.report()

    def report(self):
        # calculate average latency for all peers.
        avgs = defaultdict(lambda: None)
        reqs_served = defaultdict(lambda: 0)
        reqs_served_total = 0
        protocol = self.ctx.protocol

        start_period = self.ctx.simulation.time - REPORTING_INTERVAL
        end_period = self.ctx.simulation.time

        for request in self.requests.values():
            if not (start_period < request.timestamp <= end_period):
                continue
            
            reqs_served_total += 1
            reqs_served[request.server.id] += 1

            # weight each belief based on stake
            # weighted_rtt = protocol.staked[req.client.id]
            # TODO handle faild requests with null rtt.
            rtt = (0.25*request.client_reported_rtt + 0.75*request.server_reported_rtt) / 2
            
            curr_avg = avgs[request.server.id]
            if curr_avg is None:
                new_avg = rtt
            else:
                new_avg = (curr_avg + rtt) / 2.
            avgs[request.server.id] = new_avg
        
        protocol.report(self, avgs, reqs_served, reqs_served_total)
    
    def on_register_peer(self, peer):
        DISTANCE_THRESHOLD = 0.2
        if self.distance_to(peer) < DISTANCE_THRESHOLD:
            self.peerset.append(peer)
            return True
        return False
    
    def begin_request(self, from_peer, resource):
        # verify that the from_peer has minimum stake.
        request_id = self.requests_served + 1
        self.requests_served += 1

        request = Request(
            id_=request_id,
            timestamp=self.ctx.simulation.time,
            client=from_peer,
            server=self.find_closest_peer(),
            load_balancer=self,
            content=resource,
            client_reported_rtt=None,
            server_reported_rtt=None
        )
        self.requests[request.id] = request
        return request

    def end_request(self, id_, agent, rtt):
        # verify request<>peer
        request = self.requests[id_]
        if agent.id == request.server.id:
            request.server_reported_rtt = rtt
        if agent.id == request.client.id:
            request.client_reported_rtt = rtt
    
    def find_closest_peer(self):
        # choose random peer
        # TODO: keep track of peer performance, and choose
        # peer with best score
        if len(self.peerset) > 0:
            return choice(self.peerset)
        return self