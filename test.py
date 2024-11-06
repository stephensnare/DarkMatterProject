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
    points = gp.generate(n, 0)
    points2 = gp.generate(n, 1)

    points_all = np.concatenate((points, points2))


    node = Node(1,(1,1,1),1)

    for i in range(len(points_all)):
        node.add_point(points_all[i])

    return points_all, node


def main():
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    points, node = createAndPlace(15)

    # CoM_tracker(node)
    # allDepths, maxDepth = df(node)
    # print(maxDepth)
    plot(points, node)
    for point in node.psuedoPoint.pointPointers:
        breadth_first_force_eval(point, node, 1)
        print(point.acc)

    time = np.linspace(0, 3, 1)
    for frame in time:
        plot((points), (node), node_toggle=False)


main()