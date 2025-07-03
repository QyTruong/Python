from agents import Environment, Food, Water

class Park(Environment):
    def percept(self, agent):
        return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        if action == "move down":
            print(f'{str(agent)} decide to {action} at location: {agent.location}')
            agent.movedown()
        elif action == "eat":
            things = self.list_things_at(agent.location, tclass=Food)

            if len(things) != 0:
                if agent.eat(things[0]):
                    print(f'{str(agent)} ate {things[0]} at location: {agent.location}')
                    self.delete_thing(things[0])
        elif action == "drink":
            things = self.list_things_at(agent.location, tclass=Water)

            if len(things) != 0:
                if agent.drink(things[0]):
                    print(f'{str(agent)} drink {things[0]} at location: {agent.location}')
                    self.delete_thing(things[0])

    def is_done(self):
        super().is_done()
        return not any(isinstance(thing, Food) and isinstance(thing, Water) for thing in self.things)
