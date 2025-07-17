from tree import *
from utils import  PriorityQueue


def best_search(problem, f):
    node = Node(problem.initial)
    fringe = PriorityQueue([node], f)
    visited = {problem.initial : node}

    while fringe:
        node = fringe.pop()

        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s = child.state

            if s not in visited or child.path_cost < visited[s].path_cost:
                visited[s] = child
                fringe.add(child)
    return failure