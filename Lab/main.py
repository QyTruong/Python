from agents import *
from blind_dog1D import  *
from park1D import *

if __name__ == "__main__":

    park = Park()
    dog = BlindDog(program=program)
    food = Food()
    water = Water()


    park.add_thing(dog, 1)
    park.add_thing(food, 5)
    park.add_thing(water, 7)

    park.run(10)