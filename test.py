# Useful git terminal commands
    # Pushing to master branch on GitHub in the terminal
        # git add .
        # git commit -m "Enter a commit message"
        # git push

    # Pulling from GitHub
        # git pull

    # Restore file to previous save state
        # git restore [filepath to the file you want to restore]

import generatePoints as gp
from classes import *
from classes.node import Node
from forceEval import breadth_first_force_eval
from plotter import plot
from CoM import CoM_tracker
from depthFirst import depthFirst as df
import numpy as np

### Create and Place Points ###
def createAndPlace(n):
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    points = gp.generate(n, 0)
    points2 = gp.generate(n, 1)

    points_all = np.concatenate((points, points2))


    node = Node(1,(1,1,1),1)

    for i in range(len(points_all)):
        node.add_point(points_all[i])

    return points_all, node


def createPoints(n):
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    points1 = gp.generate(n, 0)
    points2 = gp.generate(n, 1)
    points_all = np.concatenate((points1, points2))
    return points_all


def placePoints(points, node):
    if node == None:
        node = Node(1, (1,1,1), 1)
    else:
        # Burn the node
        node = Node(1, (1,1,1), 1)

    for i in range(len(points)):
        node.add_point(points[i])

    return node


def main():
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    numpoints = 30
    theta = .5
    time = 3
    timestep = 0.5
    node_toggle = False
    points = createPoints(numpoints//2)
    node = placePoints(points, None)
    # points, node = createAndPlace(numpoints//2)

    for frame in range(0, time, timestep):
        if frame == 0:
            plot(points, node, frame, node_toggle)
        else:
            for point in node.psuedoPoint.pointPointers:
                CoM_tracker(node)
                breadth_first_force_eval(point, node, 1)
                # print(point.acc)

            plot(points, node, frame, node_toggle)


main()
