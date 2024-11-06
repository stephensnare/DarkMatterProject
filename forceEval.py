# this file should go through each point
# at each point it should do a breadthFirst evaluation of the theta parameter in each other cells
    # a condition of the breadthFirst search is that the particle of interest must not be included in the cell of interest's pointPointers
# cells accepted under the theta parameter should have their force contribution calculated
# total force and accelleration should be tracked and stored
# itterate 2-5 for every other point
import math

from classes.node import Node
from classes.point import Point

G = 6.67 * 10**-11

# theta is side length of node over distance from center of mass


def passes_theta(point: Point, child: Node, theta):
    if point in child.psuedoPoint.pointPointers:
        return False, False, False, False
    psuedo_point = child.psuedoPoint
    px = point.x
    py = point.y
    pz = point.z

    psuedo_x = psuedo_point.x
    psuedo_y = psuedo_point.y
    psuedo_z = psuedo_point.z

    rx = abs(psuedo_x - px)
    ry = abs(psuedo_y - py)
    rz = abs(psuedo_z - pz)

    l = child.side_length
    d = math.sqrt(rx ** 2 + ry ** 2 + rz ** 2)

    if l/d > theta:
        return False, False, False, False

    return d,rx,ry,rz



def breadth_first_force_eval(point: Point, node: Node, theta):
    queue = []
    poi = []
    queue.append(Node)
    while len(queue) > 0:
        node = queue.pop(0)
        for child in [node.tlf, node.trf, node.tlb, node.trb, node.blf, node.brf, node.blb, node.brb]:
            if child not in queue:
                d,rx,ry,rz = passes_theta(point, child, theta)

                if d == False:
                    queue.append(child)
                else:
                    poi.append([child.psuedoPoint,rx,ry,rz,d])

    x_force = 0
    y_force = 0
    z_force = 0
    for psuedo_info in poi:
        psuedo_point = psuedo_info[0]
        rx = psuedo_info[1]
        ry = psuedo_info[2]
        rz = psuedo_info[3]
        r_mag = psuedo_info[4]


        x_force += (rx*psuedo_point.m*G)/(r_mag**3)
        y_force += (ry*psuedo_point.m*G)/(r_mag**3)
        z_force += (rz*psuedo_point.m*G)/(r_mag**3)


        acc = [x_force, y_force, z_force]
        point.acc = acc


