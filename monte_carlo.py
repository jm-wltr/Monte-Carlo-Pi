#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:39:26 2021

@author: Jaimew
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import time
import sys

# Generate a random number from -1 to 1
def rand():
    return random.uniform(-1, 1)

# Calculate the distance of a 2D point to the origin
def distance(x, y):
    return np.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

# Determines if a 2D point is inside the unit circle.
def in_circle(x, origin = [0,0]):
    if len(x) != 2: return "x is not two-dimensional"
    elif distance(origin, x) <= 1: return 1
    else: return 0

#Calculate pi
start_time = time.perf_counter()
inside=0
R = 100000
for i in range(R):
    point = [rand(), rand()]
    inside += in_circle(point)
    if i % (R/1000) == 0:
        sys.stdout.write("\r"+ str(round(i/R*100, 2)) + "%")
sys.stdout.write("\r")

pi = inside/R*4
print(pi)

with open("pi.txt", "r") as f:
    f1 = f.read().splitlines()
pi_file = float(f1[0])
R_file = int(f1[1])

R_new = R + R_file
pi_new = (pi*R + pi_file*R_file)/R_new

with open ("pi.txt", "w") as f:
    f.write(str(pi_new)+"\n"+str(R_new))

#Show time ellapsed
end_time = time.perf_counter()    
dt = end_time-start_time
print("Calculation time: "+str(dt))   
