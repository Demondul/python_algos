import random

def randInt(min=0,max=100):
    return int(random.random()*max)+min

print(str(randInt()))
print(str(randInt(max=50)))
print(str(randInt(min=50)))
print(str(randInt(min=50,max=500)))
