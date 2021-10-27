
import abc
from abc import ABC, abstractmethod
from collections import defaultdict

class Agent(ABC):
    __metaclass__ = abc.ABCMeta
    agent_type = 'Agent'

    def __init__(self, type):
        super().__init__()
        self.agent_type = type
    
    def set_id(self, id_):
        self.id = id_

    @abstractmethod
    def step(self, i):
        pass


