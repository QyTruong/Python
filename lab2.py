import collections
import math
from typing import Set


def find_alphabetically_first_word(text : str) -> str:
    return sorted(text.split(' '))[0]

def euclidean_distance(loc1, loc2) -> float:
    x1, y1 = loc1
    x2, y2 = loc2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def manhattan_distance(loc1, loc2) -> float:
    return sum(abs(loc1[i] - loc2[i]) for i in range(len(loc1)))

def sparse_vector_dot_product(v1: collections.defaultdict, v2: collections.defaultdict) -> float:
    return sum(v1[i] * v2[i] for i in v1 if i in v2)

def increment_sparse_vector(v1: collections.defaultdict, scale: float, v2: collections.defaultdict) -> None:
    for key, value in v2.items():
        increment = scale * value
        if increment != 0:
            v1[key] += increment

def find_nonsingleton_words(text: str) -> Set[str]:
    words = text.split(' ')
    counts = collections.Counter(words)
    return {item for item in words if counts[item] < 2}


if __name__ == "__main__":
    choice = input('Your choice: ')

    match choice:
        case '1':
            text = input('Enter text: ')
            word = find_alphabetically_first_word(text)
            print(word)
        case '2':
            loc1 = (1, 2)
            loc2 = (4, 6)
            print(euclidean_distance(loc1, loc2))
        case '3':
            loc1 = (1, 2)
            loc2 = (4, 6)
            print(manhattan_distance(loc1, loc2))
        case '4':
            v1 = collections.defaultdict(float, {'a' : 5, 'b' : 7})
            v2 = collections.defaultdict(float, {'b' : 2, 'c' : 4, 'd' : 3})
            print(sparse_vector_dot_product(v1, v2))
        case '5':
            v1 = collections.defaultdict(float, {'a' : 5})
            v2 = collections.defaultdict(float, {'b' : 2, 'a' : 3})
            increment_sparse_vector(v1, 2, v2)
        case '6':
            text = input('Enter text: ')
            print(find_nonsingleton_words(text))