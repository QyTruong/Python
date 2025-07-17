import math
from collections import deque
from tree import Node, expand

def breadth_first_search(problem):
    node = Node(problem.initial)
    q = deque([node])
    visited = {problem.initial}
    res = []
    while q:
        node = q.pop()
        res.append(node.state)
        children = expand(problem, node)

        for child in children:
            s = child.state
            if problem.is_goal(s):
                res.append(s)
                return res
            if s not in visited:
                visited.add(s)
                q.appendleft(child)
    return None











