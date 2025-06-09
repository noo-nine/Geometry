import matplotlib.pyplot as plt
import numpy as np
import random

def f(x, y):
    if( r < 0.25):
        nextX = 0
        nextY = 0.16 * y
    elif( r < 0.5):
        nextX = 0.85 * x + 0.04 * y
        nextY = -0.04 * x + 0.85 * y + 1.6
    elif( r < 0.75):
        nextX = 0.20 * x - 0.26 * y
        nextY = 0.23 * x + 0.22 * y + 1.6
    else:
        nextX = -0.15 * x + 0.28 * y
        nextY = 0.26 * x + 0.24 * y + 0.44
    return nextX, nextY


plt.plot(0, 0)
x = 0
y = 0
x_list = []
y_list = []
for i in range(0, 50000):
    r = random.random()
    x_store, y_store = f(x, y)
    x_list.append(x_store)
    y_list.append(y_store)
    plt.plot(x_store, y_store, marker = 'o', color = 'green')
    x = x_store
    y = y_store

plt.show()