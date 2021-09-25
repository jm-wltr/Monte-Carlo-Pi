# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Created on Fri Sep 24 11:17:10 2021
@author: jaimewalter
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
samples = 4 #Integer: max number of samples for each repetition
reps = 1000 #Integer: n. of times we calculate pi, n. of lines in the graph
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random
import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.perf_counter()

# Generate a random number from -1 to 1
def rand():
    return random.uniform(-1, 1)

# Calculate the distance of a 2D point to the origin
def distance(x, y):
    return np.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

# Determines if a 2D point is inside the unit circle.
def in_circle(x, origin = [0,0]):
    if len(x) != 2: return "x is not two-dimensional"
    elif distance(origin, x) <= 1: return True
    else: return False

#Calculate pi
fig = plt.figure()
ax = fig.add_subplot(111)

x = list(np.logspace(1, samples, num=50, dtype=int))
pi = []
   
for times in range(1,reps):
    y = []
    inside = []
    for R in x:
        for i in range(R):
            while len(inside) < i:
                point = [rand(), rand()]
                inside.append(in_circle(point))
        y.append(sum(inside) / R * 4)       
        
    pi.append(y[-1])

    ax.plot(x, y, label = "_nolegend_") 
    #ax.plot([x[0],x[-1]], [np.pi,np.pi], color="red", marker="o", markersize = 3,linestyle = "dashed", linewidth=2, label = "$\pi$")

#Calculate mean
mean = np.mean(pi)

print("Pi: " + str(np.pi))
print("Pi approximation: " + str(mean))
print("Difference: " + str(np.pi-mean))

#Show time ellapsed
end_time = time.perf_counter()    
dt = end_time-start_time
print("Calculation time: "+str(dt))   
