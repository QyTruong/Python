
from Python.dfs import depth_first_search
from Python.ucs_search import *
from bfs import breadth_first_search
from maps import Map
from problems import RouteProblem
from tree import path_states

if __name__ == "__main__":
    # romania = Map(
    #     {('O', 'Z'): 71, ('O', 'S'): 151,
    #      ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
    #      ('L', 'T'): 111, ('L', 'M'): 70,
    #      ('D', 'M'): 75,
    #      ('C', 'D'): 120, ('C', 'R'): 146, ('C', 'P'): 138,
    #      ('R', 'S'): 80,
    #      ('F', 'S'): 99,
    #      ('B', 'F'): 211, ('B', 'P'): 101, ('B', 'G'): 90, ('B', 'U'): 85,
    #      ('H', 'U'): 98,
    #      ('E', 'H'): 86,
    #      ('U', 'V'): 142,
    #      ('I', 'V'): 92, ('I', 'N'): 87,
    #      ('P', 'R'): 97},
    #
    #     {'A': (76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294),
    #      'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
    #      'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
    #      'S': (187, 463), 'T': (83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})

    romania = Map(
        {('O', 'Z'): 71,
         ('O', 'S'): 151,
         ('A', 'Z'): 75,
         ('A', 'S'): 140,
         ('A', 'T'): 118,
         },

        {'A': (76, 497), 'O': (117, 580), 'S': (187, 463), 'T': (83, 414), 'Z': (92, 539)})

# a o s t z
    route = RouteProblem('O', 'T', map=romania)
    print(breadth_first_search(route))
    print(depth_first_search(route))
    print(path_states(uniform_cost_search(route)))

    a_star = a_star_search(route)
    print(path_states(a_star))