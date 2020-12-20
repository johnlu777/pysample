# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
'''
x_s= list(range(1,101))
y=[x**2 for x in x_s]
#plt.scatter([1,2,3,4,5],squares)
plt.scatter(x_s, y, s=5)


plt.tick_params(axis='both', which = 'major', labelsize=14)
plt.axis([0,110, 0,11000])
plt.show()
'''

from random import choice

x=[0]
y=[0]

while len(x)<500000:
    xd=choice([1, -1])
    xdis= choice([0,1,2,3])
    yd=choice([1, -1])
    ydis= choice([0,1,2,3])  
    xstep = xd*xdis
    ystep = yd*ydis
    
    if xstep == 0  and ystep == 0:
        continue
    next_x = x[-1] + xstep
    next_y = y[-1] + ystep
    x.append(next_x)
    y.append(next_y)

plt.scatter(x, y, s=1)
