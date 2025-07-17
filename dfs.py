import math
from collections import deque
from inspect import stack
from tree import Node, expand


def depth_first_search(problem):
    # Khoi tao node goc
    node = Node(problem.initial)

    # Tao queue chua node goc
    s = [node]

    # Danh dau node goc da duoc tham
    visited = {problem.initial}

    # Danh sach luu duong di
    res = []

    while s:
        # Lay node ra khoi queue de tim neighbors cua no
        node = s.pop()

        # state de the hien thi ten node thay vi dia chi
        res.append(node.state)

        # Danh sach cac neighbors
        children = expand(problem, node)

        # Duyet qua cac neighbors de tim goal
        for child in children:
            neigh = child.state

            # Neu node hien tai la goal -> ket thuc
            if problem.is_goal(neigh):
                res.append(neigh)
                return res

            # Neu chua tham thi danh dau va cho vao queue
            if neigh not in visited:
                visited.add(neigh)
                s.append(child)
    return None

def dfs(problem):
    pass


