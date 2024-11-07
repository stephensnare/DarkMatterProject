import numpy as np
from classes.point import Point
from classes.node import Node
from classes.psuedopoint import PsuedoPoint
import generatePoints as gp

def CoM_tracker(node):

    if node:
        if node.population == 0: #ignore
            return
        if node.population == 1: #assign point as Psuedopoint
            node.psuedoPoint = PsuedoPoint(node.point.x, node.point.y, node.point.z, 1)
            # node.psuedoPoint.addPointPointer(node.point)
            return

        CoM_tracker(node.tlf)
        CoM_tracker(node.trf)
        CoM_tracker(node.tlb)
        CoM_tracker(node.trb)
        CoM_tracker(node.blf)
        CoM_tracker(node.brf)
        CoM_tracker(node.blb)
        CoM_tracker(node.brb)
            
        
        if node.population > 1: #find CoM of psuedopoints
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
        return


    return
    

