import numpy as np

from classes.point import Point


def generate():
    numPoints = 10
    i = 0
    points = np.zeros_like(numPoints)
    while i < numPoints:
        points[i] = Point(1, 1, 1)

        j = 0
        while j < i:
            if (points[i].x != points[j].x) and (points[i].y != points[j].y) and (points[i].z != points[j].z):
                j += 1
            else:
                points[i] = Point()

        i += 1

        # For debugging
        # print('point x: ', point.x)
        # print('point y: ', point.y)
        # print('point z: ', point.z)
        # print('\\')


generate()