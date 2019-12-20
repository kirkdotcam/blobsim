import random

class Blob():
    def __init__(self, hunger, diet, alive):
        self.hunger = hunger
        self.diet = diet
        self.alive = alive
        self.size = random.gauss(50,30)

    def report(self):
        if self.alive:
            msg=f"""
            {self.hunger}
            {self.diet}
            {self.alive}
            {self.size}"""

            print(msg)

    def eat(self, food, population):
        # dead blobs don't eat
        if not self.alive: return

        if self.hunger:
            # eat food
            if food > 1:
                food -= 2
                self.size+=2
                self.hunger=False

            # eat another blob
            elif self.diet == "carnivore":
                victim = self

                while len(population) > 1 and victim == self:
                    victim = random.choice(population)
                
                if victim != self: # need in case there is only 1 pop
                    self.size += 0.1*victim.size
                    self.hunger = False
                    population.remove(victim)

            # starve
            else:
                self.size -= 10
        
        if not self.hunger:
            self.size -= 1
            self.hunger = True

        return food

    def survive(self, food, population):
        food = self.eat(food, population)

        if self.size < 20:
            self.alive = False

        return food
    
                

def gen_blob():

    diet = random.choice(["herbivore", "carnivore"])

    return Blob(False,diet,True)