from collections import defaultdict

def multimap(pairs):
    res = defaultdict(list)
    for key, val in pairs:
        res[key] = val
    return res

class Map:
    def __init__(self, links, locations=None, directed=False):
        if not directed:
            for v1, v2 in list(links):
                links[v2, v1] = links[v1, v2]

        self.distance = links
        self.neighbors = multimap(links)
        self.locations = locations