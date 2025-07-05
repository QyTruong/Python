import math
from collections import deque


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

cutoff = Node('cutoff', path_cost=math.inf)  # Indicates iterative deepening search was cut off.
failure = Node('failure', path_cost=math.inf)  # Indicates an algorithm couldn't find a solution.


def expand(problem, node):
    s = node.state

    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)

def breadth_first_search(problem):
    node = Node(problem.initial)
    q = deque([node])
    visited = {problem.initial}
    res = []
    while q:
        node = q.pop()
        res.append(node.state)
        print(res)
        children = expand(problem, node)

        for child in children:
            s = child.state
            if problem.is_goal(s):
                res.append(s)
                return res
            if s not in visited:
                visited.add(s)
                q.appendleft(child)












