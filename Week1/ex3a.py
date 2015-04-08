"""
Lab 1 Example 3a
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#1: Set variables

h = 800.				#Height of drop in meters
g = 9.81				#Acceleration of gravity

v = input('Input the initial velocity of the ball in meters per second: ')

t = (-v + math.sqrt((v**2)+2*g*h)) / g

print 'The ball takes',t,'seconds to reach the ground'
