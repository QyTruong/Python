from best_search import *


def greedy_search(problem, h=None):
    h = h or problem.h
    return best_search(problem, f=h)

def g(n):
    return n.path_cost

def uniform_cost_search(problem):
    return best_search(problem, f=g)




