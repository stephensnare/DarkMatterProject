import numpy as np
from classes.point import Point


def generate(numPoints, loc):
    points = np.empty(numPoints, dtype=object)

    center = [0.2, 0.2, 0.2] if loc == 0 else [0.8, 0.8, 0.8]
    spread = [0.05, 0.05, 0.05] if loc == 0 else [0.05, 0.05, 0.05]
    vel = [0.05, 0.05, 0.05] if loc == 0 else [-0.05, -0.05, -0.05]

    for i in range(numPoints):
        x = np.random.normal(center[0], spread[0])
        y = np.random.normal(center[1], spread[1])
        z = np.random.normal(center[2], spread[2])

        if x > 1:
            x = center[0]
        if y > 1:
            y = center[1]
        if z > 1:
            z = center[2]

        vel_x = vel[0] + (np.random.random(1)/50)
        vel_y = vel[1] + (np.random.random(1)/50)
        vel_z = vel[2] + (np.random.random(1)/50)
        vel0 = (vel_x[0], vel_y[0], vel_z[0])

        points[i] = Point(x, y, z, vel0)

    return points