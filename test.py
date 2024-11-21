# Useful git terminal commands
    # Pushing to master branch on GitHub in the terminal
        # git add .
        # git commit -m "Enter a commit message"
        # git push
import time

from matplotlib import pyplot as plt

# Pulling from GitHub
        # git pull

    # Restore file to previous save state
        # git restore [filepath to the file you want to restore]

import generatePoints as gp
from classes import *
from classes.node import Node
from classes.point import Point
from forceEval import breadth_first_force_eval
from plotter import plot
from CoM import CoM_tracker
from depthFirst import depthFirst as df
import numpy as np

### Create and Place Points ###
def createPoints(n):
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]

    points1 = gp.generate(0, 2)
    points0 = gp.generate(n, 1)
    points2 = gp.generate(n, 0)
    points_all = np.concatenate( (points0, points2,points1) )
    # points_all  = points1
    return points_all

def calculate_frames(time,timestep,points,node_toggle,theta,node):
    for frame in range(0, int(time / timestep)):
        if frame == 0:
            plot(points, node, frame, node_toggle)

        else:
            CoM_tracker(node)
            for point in points:
                breadth_first_force_eval(point, node, theta)
            node.burn_tree()
            for point in points:
                point.update_params(timestep)
            node = Node(1, (1, 1, 1), 1)
            node.placePoints(points)
            plot(points, node, frame, node_toggle)


def main():
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    numpoints = [20,30,40,50,60,70,80,90,100,120,140,160,180,200,220,240,260,280,300,350,400,500]
    maxtime = 10

    timestep = .05
    node_toggle = False
    points = createPoints(100//2)
    node = Node(1, (1,1,1), 1)
    node.placePoints(points)

    calculate_frames(maxtime,timestep,points,node_toggle,0,node)




    ########### TIME COMPLEXITY ANALYSIS #############

    # t0_times = []
    # t1_times = []
            
    # for num in numpoints:
    #     print(f'calculating keplar n={num} ')
    #     points = createPoints(num // 2)
    #     node = Node(1, (1, 1, 1), 1)
    #     node.placePoints(points)
    #     start_time = time.perf_counter()
    #     calculate_frames(maxtime, timestep, points, node_toggle, 0, node)
    #     total_time = time.perf_counter() - start_time
    #     t0_times.append(total_time)
    #
    #
    # for num in numpoints:
    #     print(f'calculating BH n={num} ')
    #     points = createPoints(num // 2)
    #     node = Node(1, (1, 1, 1), 1)
    #     node.placePoints(points)
    #
    #     start_time = time.perf_counter()
    #     calculate_frames(maxtime, timestep, points, node_toggle, 1, node)
    #     total_time = time.perf_counter() - start_time
    #
    #     t1_times.append(total_time)
    #
    #
    # plt.figure()
    # plt.title("Computational Time for Keplar vs Barnes Hut Algorithm")
    # plt.plot(numpoints,t0_times, color="orange",marker="o",label="Keplar Algorithm, O(N^2")
    # plt.plot(numpoints,t1_times, color="blue",marker="o",label="BH Algorithm, O(N*logN)")
    # plt.xlabel("Number of points")
    # plt.ylabel("Time (s)")
    # plt.legend()
    #
    # plt.show()

    ############## ERROR CALCULATION ##############

    # points = createPoints(500)
    # poi: Point = points[0]
    # thetas = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2]
    # errors = []
    #
    #
    # node = Node(1, (1, 1, 1), 1)
    # node.placePoints(points)
    # CoM_tracker(node)
    # breadth_first_force_eval(poi, node, 0.0)
    # actual_force = poi.acc
    # print('actual', actual_force)
    # node.burn_tree()
    #
    # for theta in thetas:
    #     node = Node(1, (1, 1, 1), 1)
    #     node.placePoints(points)
    #     CoM_tracker(node)
    #     breadth_first_force_eval(poi, node, theta)
    #     approx_force = poi.acc
    #     v = np.sqrt(actual_force[0]**2 + actual_force[1]**2 + actual_force[2]**2)
    #
    #     errorx = approx_force[0] - actual_force[0]
    #     errory = approx_force[1] - actual_force[1]
    #     errorz = approx_force[2] - actual_force[2]
    #     rel_error = np.sqrt(errorx**2 + errory**2 + errorz**2)/v
    #     errors.append(rel_error)
    #     node.burn_tree()
    #
    #
    # plt.figure()
    # plt.title("Error as a function of theta")
    # plt.xlabel("theta")
    # plt.ylabel("Vector distance between actual and approximate force on point P")
    # plt.plot(thetas,errors)
    # plt.scatter(thetas,errors)
    # plt.show()

main()
