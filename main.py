# from src import Blob as b
from src import Simulation as Sim

sim = Sim.Simulation()

print(next(sim.irun(days=100)))
# sim.report()
