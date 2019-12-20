import Blob as b


population = b.gen_population(200)

for x in range(1000):
    for blob in population:
        # print(population)
        blob.survive(population)
        

for blob in population:
    if blob.alive:
        blob.report()
print(len(population))