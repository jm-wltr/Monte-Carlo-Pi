import random
import math
import matplotlib.pyplot as plt

def rand():
    return random.uniform(-1, 1)

def distance(x, y):
    return math.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

def in_circle(x, origin = [0,0]):
    if len(x) != 2: return "x is not two-dimensional"
    elif distance(origin, x) <= 1: return True
    else: return False

inside=[]
R = 10000
for i in range(R):
    point = [rand(), rand()]
    inside.append(in_circle(point))

print(sum(inside) / R * 4)
