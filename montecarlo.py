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

def rand():
    return random.uniform(-1, 1)

def distance(x, y):
    return np.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

def in_circle(x, origin = [0,0]):
    if len(x) != 2: return "x is not two-dimensional"
    elif distance(origin, x) <= 1: return True
    else: return False

x = list(np.logspace(2, 7, num=100, dtype=int))
y = []

start_time = time.perf_counter()
inside = []
for R in x:
    for i in range(R):
        while len(inside) < i:
            point = [rand(), rand()]
            inside.append(in_circle(point))
    #print(len(inside))
    y.append(sum(inside) / R * 4)
end_time = time.perf_counter()        
    
print(y[-1])

dt = end_time-start_time
print()
print(dt)

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_xscale("log")
ax.plot(x, y)
