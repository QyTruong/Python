import  collections
import math

class Positon():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_alphabetically_first_word(s:str) -> str:
    res = sorted(s.split(' '))
    return res[0];

def euclidean_distance(loc1 : Positon, loc2 : Positon) -> float:
    return math.sqrt((loc2.x - loc1.x)**2 + (loc2.y - loc1.y)**2)

def manhattan_distance2D(loc1 : Positon, loc2 : Positon) -> float:
    return (abs(loc1.x - loc2.x) + abs(loc1.y - loc2.y));


if __name__ == '__main__':
    print('Cau 1:')
    print(find_alphabetically_first_word("toi thuc hanh tri tue nhan tao"))

    print('Cau 2:')
    loc1 = Positon(1,2)
    loc2 = Positon(4,6)
    print(euclidean_distance(loc1, loc2))

    print('Cau 3:')
    print(manhattan_distance2D(loc1, loc2))




