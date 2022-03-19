# example of the code
import math
import random
import matplotlib.pyplot as plt
import time
# input parameters for drone
V = 1 # drone speed per second
R = 10 # radius how far drone can see
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
print(euclidean_distance(30,2,2,30))

#check if drone is in range of fire
if euclidean_distance(hotspot_XY[0],hotspot_XY[1],drone_XY[0][0],drone_XY[0][1]) > 10:
    # if direction is TRUE the drone will go right. if FALSE it will go left. if NONE it will not move in the x direction
    direction = True
    change_direction = 0

    for drone in range(150):
        movement = 1
        print(change_direction)
        
        
        #drone will move up
        if change_direction < 10: 
            drone_XY.append(tuple((drone_XY[-1][0],drone_XY[-1][1] + movement)))
            
        # turn left
        elif change_direction > 10:
            
            if direction == True:
                # the drone is on the left border
                drone_XY.append(tuple((drone_XY[-1][0] + movement,drone_XY[-1][1])))
                
                if drone_XY[-1][0] > width:
                    change_direction = 0
                    direction = False
                    
            if direction == False: 
                drone_XY.append(tuple((drone_XY[-1][0] - movement,drone_XY[-1][1])))
                
                if drone_XY[-1][0] <= 0:
                    change_direction = 0
                    direction = True
        
        
        
        change_direction += movement         

    

# example of your output – list of tuple with coordinates
#drone_XY = [(0.0, 0.0),
#(0.7, 0.7),
#(0.7, 1.7),
#(0.7, 2.7),
#(1.7, 2.7),
#(25,25),
#(25,10)]
# code to plot drone trajectory

xs, ys = zip(*drone_XY)
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, depth)
ax.plot(xs, ys, 'o--', lw=2, color='black', ms=1)
ax.plot(hotspot_XY[0], hotspot_XY[1], 'o', lw=2, color='red', ms=10)