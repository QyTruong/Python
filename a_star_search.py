from best_search import *


def a_star_search(problem, h=None):
    h = h or problem.h
    return best_search(problem, f=lambda n: g(n) + h(n))


