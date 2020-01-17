from .Blob import Blob

class Simulation():
    
    def __init__(self, members=200, food=20000):
        self.population = Blob.gen_population(self,members=members, food=food)
        self.current_day = 0

    def current_config(self):
        print(self.__dict__)

    
    def irun(self, days = 10):
        print("begin run")

        for day in range(days):
            self.current_day += 1

            for blob in self.population:
                blob.survive(self.population)

            yield [blob.report() for blob in self.population]

    def run(self, **kwargs):
        return list(self.irun(**kwargs))
    
    def report(self):
        for blob in self.population:
            print(blob.report())

