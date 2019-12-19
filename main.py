import random

food = 100

while True:
    
    if food < 1:
        print("blob dies")
        exit()
    else:
        food-=1
        print(food)
