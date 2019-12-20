from src import Blob as b


population = b.gen_population(200, food=20000)

for x in range(10):
    for blob in population:
        # print(population)
        blob.survive(population)
for blob in population:
    if blob.alive:
        print(blob.report())
print(len(population))
