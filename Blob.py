import random

class Blob():

    resources = {}

    def __init__(self, hunger, diet, alive, food):
        self.hunger = hunger
        self.diet = diet
        self.alive = alive
        self.size = random.gauss(50,30)
        self.resources["food"] = food

    def report(self):
        msg=f"""
        {self.hunger}
        {self.diet}
        {self.alive}
        {int(self.size)}"""

        print(msg)

    def eat(self, population):
        food = self.resources["food"]
        # dead blobs don't eat
        if not self.alive: return food

        if self.hunger:
            # eat food
            if food > 1:
                food -= 2
                self.size+=2
                self.hunger=False

            # eat another blob
            elif self.diet == "carnivore":
                tempPop = population.copy()
                tempPop.remove(self)
                victim = self
                while len(population) > 1 and victim.alive == False:
                    victim = random.choice(tempPop)
                    tempPop.remove(victim)
                
                if victim != self: # need in case there is only 1 pop
                    self.size += 0.1*victim.size
                    self.hunger = False
                    victim.alive = False
                    print("eaten")
                    victim.report()

            # starve
            else:
                self.size -= 10
        
        if not self.hunger:
            self.size -= 1
            self.hunger = True

        # death by starvation
        if self.size < 20:
            self.alive = False
            print("starved to death")
            self.report()

        return food

    def survive(self, population):
        self.resources["food"] = self.eat(population)

        return self.resources["food"]
    
                

def gen_blob(food):

    diet = random.choice(["herbivore", "carnivore"])

    return Blob(False,diet,True,food)

def gen_population(num, **kwargs):
    food=kwargs.get("food",1000)
    return [gen_blob(food) for i in range (num)]