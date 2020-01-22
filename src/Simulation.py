from .Blob import Blob
from copy import deepcopy


class Simulation():

    def __init__(self, members=200, food=20000):
        self.population = Blob.gen_population(self, members=members, food=food)
        self.current_day = 0

    def current_config(self):
        print(self.__dict__)

    def run_day(self):

        self.current_day += 1

        for blob in self.population:
            blob.survive(self.population)

        return [blob.report() for blob in self.population]

    def run(self, **kwargs):
        results = []
        days = kwargs.get("days", 30)

        for x in range(days):
            results.append(deepcopy(self.run_day()))

        return results

    def report(self):
        for blob in self.population:
            print(blob.report())