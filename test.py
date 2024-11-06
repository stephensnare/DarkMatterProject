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
import numpy as np
# import animationTest as animate

from classes import *
from classes.node import Node
from plotter import plot
from CoM import CoM_tracker
from depthFirst import depthFirst as df

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

    time = np.linspace(0, 3, 1)
    for frame in time:
        plot((points_1, points_2), (node_1, node_2), node_toggle=False)


main()