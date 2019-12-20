import random

class Blob():

    resources = {}

    def __init__(self, hunger, diet, **kwargs):

        size_mu = kwargs.get("avg_size",50)
        size_sigma = kwargs.get("size_std", 30)
        food = kwargs.get("food", 1000)

        self.hunger = hunger
        self.diet = diet
        self.alive = True
        self.size = random.gauss(size_mu,size_sigma)
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
    
                

def gen_blob(**kwargs):

    diet = kwargs.get("diet",random.choice(["herbivore", "carnivore"]))

    return Blob(False,diet, **kwargs)

def gen_population(num=200, **kwargs):
    return [gen_blob(**kwargs) for i in range (num)]