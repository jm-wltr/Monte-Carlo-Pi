#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:15:18 2022

@author: Jaimew
"""

from random import uniform as rd
import numpy as np
import time
import sys

def in_circle():
    if rd(0,1)**2+rd(0,1)**2 <= 1: return 1
    else: return 0
    
R = 10000000
inside = 0

start_time = time.perf_counter()
for i in range(R):
    inside = inside + in_circle()
    if i % (R/1000) == 0:
        sys.stdout.write("\r"+ str(round(i/R*100, 2)) + "%")
sys.stdout.write("\r")

pi = inside/R*4
print(pi)

try:
    with open("pi.txt", "r") as f:
        f1 = f.read().splitlines()
    pi_file = float(f1[0])
    R_file = int(f1[1])
except:
    with open("pi.txt", "w+") as f:
        pass
    pi_file = 0.0
    R_file = 0

R_new = R + R_file
pi_new = (pi*R + pi_file*R_file)/R_new

with open ("pi.txt", "w") as f:
    f.write(str(pi_new)+"\n"+str(R_new))
    
print(pi_new)
print(np.pi - pi_new)

#Show time ellapsed
end_time = time.perf_counter()    
dt = end_time-start_time
print("Calculation time: "+str(dt))   
 
