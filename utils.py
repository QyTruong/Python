import heapq

def straight_line_distance(A, B): # A(xa, ya) B(xb, yb)
    return sum(abs(b-a)**2 for (a, b) in zip(A, B)) ** 0.5


class PriorityQueue:
    def __init__(self, items=(), key=lambda x : x):
        self.key = key
        self.items = []
        for item in items:
            self.add(item)

    def add(self, val):
        pair = (self.key(val), val)
        heapq.heappush(self.items, pair)

    def pop(self):
        return heapq.heappop(self.items)[1]

