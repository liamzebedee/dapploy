
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


