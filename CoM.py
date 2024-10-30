import numpy as np
from classes.point import Point
from classes.node import Node
from classes.psuedopoint import PsuedoPoint
import generatePoints as gp

# def main():
#     # initalize everything
#     points = gp.generate(30,1)

#     node = Node(1,(1,1,1),1)

#     for i in range(len(points)):
#         print(i)
#         point = points[i]
#         node.add_point(point)
#     # run the tracker:
#     CoM_tracker(points, node)

def CoM_tracker(node):
    # find max depth:

    # work up depth assigning CoM at each step by averageing the CoM of child cells
    

    ############################----or----################################
    # if node is 0 pop ignore
    # if node is 1 pop assign point's postion as CoM
    if node:
        if node.population == 0:
            pass
        if node.population == 1:
            node.psuedoPoint = PsuedoPoint(node.point.x, node.point.y, node.point.z, 1)
            node.psuedoPoint.addPointPointer(node.point)
            pass

        CoM_tracker(node.tlf)
        CoM_tracker(node.trf)
        CoM_tracker(node.tlb)
        CoM_tracker(node.trb)
        CoM_tracker(node.blf)
        CoM_tracker(node.brf)
        CoM_tracker(node.blb)
        CoM_tracker(node.brb)
            
        
        if node.population > 1:
            psuedo = [node.tlf.psuedoPoint, node.trf.psuedoPoint, node.tlb.psuedoPoint,
                      node.trb.psuedoPoint, node.blf.psuedoPoint, node.brf.psuedoPoint,
                      node.blb.psuedoPoint, node.brb.psuedoPoint]
            x = np.zeros(len(psuedo))
            y = np.zeros(len(psuedo))
            z = np.zeros(len(psuedo))
            m = np.zeros(len(psuedo))
            xp, yp, zp = 0,0,0
            for i in range(len(psuedo)):
                x[i] = psuedo[i].x
                y[i] = psuedo[i].y
                z[i] = psuedo[i].z
                m[i] = psuedo[i].m
                xp += x[i] * m[i]
                yp += y[i] * m[i]
                zp += z[i] * m[i]
            xp /= sum(m)
            yp /= sum(m)
            zp /= sum(m)

            node.psuedoPoint = PsuedoPoint(xp,yp,zp,sum(m))

        print(node.depth)

    # if node is >1 pop, try again for each child cell
        # once we iterate to the 1 pop cell

    # how do we then go back up and assign CoM to boxes we skipped?

    pass
    

