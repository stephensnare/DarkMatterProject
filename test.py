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
from plotter import plot
from CoM import CoM_tracker
from depthFirst import depthFirst as df

### Create and Place Points ###
def createAndPlace(loc):
    points = gp.generate(10, loc)

    node = Node(.5,(1,1,1),1)

    for i in range(len(points)):
        node.add_point(points[i])

    return points, node


def main():
    # Location 0 is [0.2, 0.2,  0.2], location 1 = [0.8, 0.8, 0.8]
    points_1, node_1 = createAndPlace(0)
    points_2, node_2 = createAndPlace(1)

    # CoM_tracker(node)
    # allDepths, maxDepth = df(node)
    # print(maxDepth)
    plot((points_1, points_2), (node_1, node_2))


main()