import numpy as np
from classes.point import Point
from classes.node import Node
import generatePoints as gp

def main():
    # initalize everything
    points = gp.generate(30,1)

    node = Node(1,(1,1,1),1)

    for i in range(len(points)):
        print(i)
        point = points[i]
        node.add_point(point)
    # run the tracker:
    CoM_tracker(points, node)

def CoM_tracker(points, node):
    # find max depth:

    # work up depth assigning CoM at each step by averageing the CoM of child cells

    ############################----or----################################
    # if node is 0 pop ignore
    # if node is 1 pop assign point's postion as CoM

    # if node is >1 pop try again for each child cell
        # once we iterate to the 1 pop cell

    # how do we then go back up and assign CoM to boxes we skipped?
    

