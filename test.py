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
def createAndPlace():
    points = gp.generate(10,0)

    node = Node(.5,(1,1,1),1)

    for i in range(len(points)):
        point = points[i]
        node.add_point(point)

    return points, node


def main():
    points, node = createAndPlace()
    CoM_tracker(node)
    allDepths, maxDepth = df(node)
    print(maxDepth)
    plot(points, node)


main()