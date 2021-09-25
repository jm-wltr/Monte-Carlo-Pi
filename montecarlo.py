# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:17:10 2021
@author: jaimewalter
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.perf_counter()

def rand():
    return random.uniform(-1, 1)

def distance(x, y):
    return np.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

def in_circle(x, origin = [0,0]):
    if len(x) != 2: return "x is not two-dimensional"
    elif distance(origin, x) <= 1: return True
    else: return False

x = list(np.logspace(1, 4, num=50, dtype=int))

fig = plt.figure()
ax = fig.add_subplot(111)
pi = []
#ax.set_xscale("log") 
   
for times in range(1,1000):
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
    #ax.plot([x[0],x[-1]], [np.pi,np.pi],
    #        color="red", marker="o", markersize = 3,linestyle = "dashed", linewidth=2, label = "$\pi$")



sd0 = np.mean(pi)

sd = np.std(pi)

lenTotal = len(pi)
pi_sd1 = [a for a in pi if a<=sd0+sd and a>=sd0-sd]
pi_sd2 = [a for a in pi if a<=sd0+2*sd and a>=sd0-2*sd]

sd1 = np.mean(pi_sd1)
sd2 = np.mean(pi_sd2)

print("Pi: " + str(np.pi))
print()
print("Pi approximate: " + str(pi[-1]))
print("Distance: "+ str(np.pi-pi[-1]))
print()
print("Pi mean: " + str(sd0))
print("Distance: " + str(np.pi-sd0))
print()
print("Pi mean (1sd): " + str(sd1))
print("Distance: " + str(np.pi-sd1))
print()
print("Pi mean (2sd): " + str(sd2))
print("Distance: " + str(np.pi-sd2))
print()
print("SD: " + str(sd))
print(str(len(pi)) + ", " + str(len(pi_sd1))+ ", " + str(len(pi_sd2)))

end_time = time.perf_counter()    

dt = end_time-start_time
print(dt)   
