import random

class Blob():
    def __init__(self, hunger, diet, alive):
        self.hunger = hunger
        self.diet = diet
        self.alive = alive

    def eat(self, food, population):
        if not self.alive: return

        if self.hunger:
            if food > 1:
                food -= 2
                self.hunger=False
            elif self.diet == "carnivore":
                victim == self
                while victim == self:
                    victim = random.choice(population)
                population.remove(victim)
        
        if not self.hunger:
            self.hunger = True

        return food
    
                

def gen_blob():

    diet = random.choice(["herbivore", "carnivore"])

    return Blob(False,diet,True)