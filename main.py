# from src import Blob as b
from src import Simulation as Sim

sim = Sim.Simulation()

print(sim.population[0].__dict__)
# print(sim.population[0])
data = sim.run(days=10)
