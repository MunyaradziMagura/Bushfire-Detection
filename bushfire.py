# example of the code
import matplotlib.pyplot as plt
import math
import random
# used to manage 1 second time delay
import time
# input parameters for drone
V = 1  # drone speed per second
R = 10  # radius how far drone can see
drone_XY = [(0.0, 0.0)]  # initial coordinates of the drone
# input parameters for map and hotspot
width, depth = 50, 50
hotspot_XY = (width * random.random(), depth * random.random())
# your main code here

for position in range(0,1200):
    # we observe drone over 1 second intervals
    time.sleep(1)
    print(position)


# example of your output – list of tuple with coordinates
drone_XY = [(0.0, 0.0),
            (0.7, 0.7),
            (0.7, 1.7),
            (0.7, 2.7),
            (1.7, 2.7)]
# code to plot drone trajectory
xs, ys = zip(*drone_XY)
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, depth)
ax.plot(xs, ys, 'o--', lw=2, color='black', ms=3)
ax.plot(hotspot_XY[0], hotspot_XY[1], 'o', lw=2, color='red', ms=10)
