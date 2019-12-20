import random

class Blob():
    def __init__(self, hunger, diet, alive):
        self.hunger = hunger
        self.diet = diet
        self.alive = alive

    def report(self):
        if self.alive:
            msg=f"""
            {self.hunger}
            {self.diet}
            {self.alive}"""

            print(msg)

    def eat(self, food, population):
        if not self.alive: return

        if self.hunger:
            if food > 1:
                food -= 2
                self.hunger=False
            elif self.diet == "carnivore":
                victim = self

                while victim == self and len(population) > 1:
                    victim = random.choice(population)
                
                if victim != self:
                    population.remove(victim)
        
        if not self.hunger:
            self.hunger = True

        return food
    
                

def gen_blob():

    diet = random.choice(["herbivore", "carnivore"])

    return Blob(False,diet,True)