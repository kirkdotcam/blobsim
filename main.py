import random

food = 100
population = []

for x in range(5):
    population.append({
        "hungry":True,
        "type":"herbivore",
        "alive":True
    })

def eat(blob):
    global food

    if blob["hungry"]:
        if blob["alive"] and food > 1:
            food -= 2
            print(food)
        else:
            blob["alive"] = False
            print(population)
            exit()

    if blob["alive"] and not blob["hungry"]:
        blob["hungry"] = True

while True:
    for blob in population:
        eat(blob)

