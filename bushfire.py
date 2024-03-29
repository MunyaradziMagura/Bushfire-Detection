# example of the code
import math
import random
import matplotlib.pyplot as plt
import time
# input parameters for drone
V = 1 # drone speed per second
R = 10 # radius how far drone can see
Fuel = 1200
drone_XY = [(0.0, 0.0)] # initial coordinates of the drone
# input parameters for map and hotspot
width, depth = 50, 50
hotspot_XY = (width * random.random(), depth * random.random())
# your main code here
target_x, target_y = zip(*drone_XY)
fig, ax = plt.subplots()
    
#check if point is in radius 
def euclidean_distance(target_x,target_y,drone_x,drone_y):
    return math.sqrt((target_x-drone_x)**2+(target_y-drone_y)**2)

#check if drone is in range of fire
if euclidean_distance(hotspot_XY[0],hotspot_XY[1],drone_XY[0][0],drone_XY[0][1]) > R:
    # if direction is TRUE the drone will go right. if FALSE it will go left
    direction = True
    change_direction = 0

    for drone in range(Fuel):
        # check if fire has been found
        if euclidean_distance(hotspot_XY[0],hotspot_XY[1],drone_XY[-1][0],drone_XY[-1][1]) <= R :
            break
        
        # drone has no more fuel
        if drone > Fuel:
            print("out of fuel...drone has crashed, starting another fire on impact")
            break
        
        # check the drone is still in bounds
        if drone_XY[-1][1] <= depth:
            movement = 1
            #drone will move up
            if change_direction < R: 
                drone_XY.append(tuple((drone_XY[-1][0],drone_XY[-1][1] + movement)))
                
            
            elif change_direction > R:
                # turn right
                if direction == True:
                    # the drone is on the left border
                    drone_XY.append(tuple((drone_XY[-1][0] + movement,drone_XY[-1][1])))
                    # check if the drone is out of bounds
                    if drone_XY[-1][0] > width:
                        change_direction = 0
                        direction = False
                # turn left
                if direction == False: 
                    drone_XY.append(tuple((drone_XY[-1][0] - movement,drone_XY[-1][1])))
                    
                    if drone_XY[-1][0] <= 0:
                        change_direction = 0
                        direction = True
            change_direction += movement         

if euclidean_distance(hotspot_XY[0],hotspot_XY[1],drone_XY[-1][0],drone_XY[-1][1]) <= R :
    print("\ndrone location")
    print(drone_XY[-1])
    print("\neuclidean distance")
    print(euclidean_distance(hotspot_XY[0],hotspot_XY[1],drone_XY[-1][0],drone_XY[-1][1]))
    print("\nfire location")
    print(hotspot_XY)
    print("\ndrone took " + str(len(drone_XY)) + " seconds or ~" +str(round(len(drone_XY) / 60, 2) ) + " minutes to find the fire")
    print("\ndrone path")
    print(drone_XY)

# code to plot drone trajectory

xs, ys = zip(*drone_XY)
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, depth)
ax.plot(xs, ys, 'o--', lw=2, color='black', ms=1)
ax.plot(hotspot_XY[0], hotspot_XY[1], 'o', lw=2, color='red', ms=10)