# this file should go through each point
# at each point it should do a breadthFirst evaluation of the theta parameter in each other cells
# a condition of the breadthFirst search is that the particle of interest must not be included in the cell of interest's pointPointers
# cells accepted under the theta parameter should have their force contribution calculated
# total force and accelleration should be tracked and stored
# itterate 2-5 for every other point
import math

from classes.node import Node
from classes.point import Point

# G = 6.67 * 10 ** -11
# WE KNOW THAT G IS NOT 0.001, HOWEVER, WE NEEDED LARGER FORCES TO SEE ACCELLERATIONS IN REAL TIME
G = 0.001


# theta is side length of node over distance from center of mass
def dl_calc(point: Point, child: Node):
    psuedo_point = child.psuedoPoint
    px = point.x
    py = point.y
    pz = point.z

    psuedo_x = psuedo_point.x
    psuedo_y = psuedo_point.y
    psuedo_z = psuedo_point.z

    rx = (psuedo_x - px)
    ry = (psuedo_y - py)
    rz = (psuedo_z - pz)

    l = child.side_length
    d = math.sqrt(rx ** 2 + ry ** 2 + rz ** 2)
    return d, l, rx, ry, rz

def passes_theta(point: Point, child: Node, theta):
    if child:
        if child.population == 1:
            if point in child.psuedoPoint.pointPointers:
                # print('1: Self Force')
                return True, True, True, True
            else: 
                # print('1: Single pop, non-self')
                d, l, rx, ry, rz = dl_calc(point, child)
                return d, rx, ry, rz
        elif point in child.psuedoPoint.pointPointers:
            # print('1: Point in cell')
            return False, False, False, False
        
        d, l, rx, ry, rz  = dl_calc(point, child)

        if d == 0:
            # print('1: Distance equaled zero???')
            return True, True, True, True

        if l / d > theta:
            # print('1: Failed Theta parameter')
            return False, False, False, False
        # print('1: including calculation')
        return d, rx, ry, rz
    else:
        # print('1: Node doesnt exist')
        return False, False, False, False


def breadth_first_force_eval(point: Point, node: Node, theta):
    queue = []
    poi = []
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        if node:
            for child in [node.tlf, node.trf, node.tlb, node.trb, node.blf, node.brf, node.blb, node.brb]:
                if child not in queue:
                    d, rx, ry, rz = passes_theta(point, child, theta)

                    if d == False:
                        # print('2 lets look at children')
                        queue.append(child)
                        pass
                    elif d == True:
                        # print('2 dead end')
                        pass
                    else:
                        # print('2 poi detected')
                        poi.append([child.psuedoPoint, rx, ry, rz, d])
                        pass

    x_force = 0
    y_force = 0
    z_force = 0
    for psuedo_info in poi:
        psuedo_point = psuedo_info[0]
        rx = psuedo_info[1]
        ry = psuedo_info[2]
        rz = psuedo_info[3]
        r_mag = psuedo_info[4]

        x_force += (rx * psuedo_point.m * G) / (r_mag ** 3)
        y_force += (ry * psuedo_point.m * G) / (r_mag ** 3)
        z_force += (rz * psuedo_point.m * G) / (r_mag ** 3)

        acc = [x_force, y_force, z_force]
        point.acc = acc
