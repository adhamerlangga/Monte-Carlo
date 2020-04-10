# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:44:49 2020

@author: ASUS
"""

from numpy import random
import matplotlib.pyplot as plt

d = 1000000 #dart
hit = 0 #dart pada daerah lingkaran
Ld = 0 #dart dilempar

xlingkaran = []
ylingkaran = []

xkotak = []
ykotak = []

    
while Ld<= d:
    xrand = random.uniform(0,1)
    yrand = random.uniform(0,1)
    Ld += 1
    if (xrand**2 + yrand**2 <= 1):
        hit += 1
        xlingkaran.append(xrand)
        ylingkaran.append(yrand)
    else:
        xkotak.append(xrand)
        ykotak.append(yrand)

pi = 4 * hit / d

print ("pi = ", pi)

#visual lingkaran pada kotak
plt.plot(xlingkaran,ylingkaran,'b.')
plt.plot(xkotak,ykotak,'r.')
plt.grid()

