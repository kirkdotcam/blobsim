import random

class Blob():

    resources = {}

    def __init__(self, diet, **kwargs):

        size_mu = kwargs.get("avg_size",50)
        size_sigma = kwargs.get("size_std", 30)
        food = kwargs.get("food", 1000)

        self.hunger = False
        self.diet = diet
        self.alive = True
        # TODO: allow other distributions of size
        self.size = random.gauss(size_mu,size_sigma)
        self.resources["food"] = food

    def print_report(self):
        """
            Simple implementation of Blob self-reporting. Prints to terminal.        
        """
        msg=f"""
        Hunger: {self.hunger}
        Diet: {self.diet}
        Alive: {self.alive}
        Size (Int) {int(self.size)}"""

        print(msg)
    
    def report(self):
        """returns dict of properties."""

        return self.__dict__

    def eat(self, population):
        """
            Allows blobs to eat, needs to be passed population for instances of carnivores and dendrivores finding food sources.

            Args:
                population(list) - list of all Blob members that may be eaten

            Returns:
                food - current food resource level
        """
        
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
                try:
                    tempPop.remove(self)
                except:
                    pass
                victim = self
                while len(population) > 1 and victim.alive == False:
                    victim = random.choice(tempPop)
                    tempPop.remove(victim)
                
                if victim != self: # need in case there is only 1 pop
                    self.size += 0.1*victim.size
                    self.hunger = False
                    victim.alive = False

            # starve
            else:
                self.size -= 10
        
        if not self.hunger:
            self.size -= 1
            self.hunger = True

        # death by starvation
        if self.size < 20:
            self.alive = False

        self.resources["food"] = food
        return food

    def survive(self, population):
        """
            Initiates survival process. Starts by eating (implemented as Blob.eat()) then moving on to other functions. You should call survive() rather than the individual functions unless you want to implement your own survival process. 

            Args:
                population(list) - list of candidates that can be eaten by carnivores and dendrivores
            
            Returns:
                food(int) - current food resource level
        
        """
        self.resources["food"] = self.eat(population)

        return self.resources["food"]
    
                

def gen_blob(**kwargs):
    """
        Generates blob objects.

        Args:
            **kwargs
                diet(str) - any of "herbivore","carnivore" FUTURE IMPLEMENTATION: "dendrivore","omnivore"

                others: see gen_population() function.

        Returns:
            Blob(object)
    """

    diet = kwargs.get("diet",random.choice(["herbivore", "carnivore"]))

    return Blob(diet, **kwargs)

def gen_population(members=200, **kwargs):
    """
        Generates a population of blobs using the gen_blob function. 

        Args:
            **kwargs
                avg_size(int or float) - mean for gaussian distribution of sizes. Defaults to 50.
                size_std(int or float) - standard deviation for gaussian distribution of sizes, defaults to 30
                food(int or float) - Starting amount of food - defaults to 1000


    """

    return [gen_blob(**kwargs) for i in range (members)]