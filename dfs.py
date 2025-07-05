import math
from collections import deque


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

cutoff = Node('cutoff', path_cost=math.inf)  # Indicates iterative deepening search was cut off.
failure = Node('failure', path_cost=math.inf)  # Indicates an algorithm couldn't find a solution.

