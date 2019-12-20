import Blob as b

# print(dir(b))
food = 100

population = [b.gen_blob() for x in range(20)]

# print(population)

for x in range(100):
    for blob in population:
        # print(population)
        food = blob.eat(food,population)
        

for blob in population:
    blob.report()