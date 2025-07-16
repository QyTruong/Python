import math
from collections import deque
from inspect import stack


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = None
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

cutoff = Node('cutoff', path_cost=math.inf)  # Indicates iterative deepening search was cut off.
failure = Node('failure', path_cost=math.inf)  # Indicates an algorithm couldn't find a solution.

def expand(problem, node):
    # state de lay ra ten node -> co the tuong tac voi map
    cur = node.state

    # Duyet qua cac canh ke
    for action in problem.actions(cur):
        # Kiem tra cur co neighbors hay khong ?
        neigh = problem.result(cur, action)
        # Gia tri tu cur -> neighbor
        cost = problem.action_cost(cur, action, neigh)
        # yield -> luu nhu 1 danh sach sau do tra ve 1 luot
        yield Node(neigh, node, action, cost)


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




