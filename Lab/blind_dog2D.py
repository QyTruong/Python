from agents import Agent, Food, Water

def program(percepts):
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'


class BlindDog2D(Agent):
    location = [0,0]
    direction = Direction('down')

    def movedown(self):
        self.location[1] += 1

    def eat(self, thing):
        if isinstance(thing, Food):
            return True
        return False

    def drink(self, thing):
        if isinstance(thing, Water):
            return True
        return False