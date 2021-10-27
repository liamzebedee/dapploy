from random import random, choice
import math

class NetworkedNode:
    def __init__(self):
        super().__init__()
        self.position = [random()]
    
    def distance_to(self, node):
        return math.dist(node.position, self.position)

