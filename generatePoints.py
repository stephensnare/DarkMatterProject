import numpy as np

from classes.point import Point


def generate():
    numPoints = 10
    points = np.zeros_like(numPoints)


    i = 0
    while i < numPoints:
        # Creates a new point
        # Currently 1, 1, 1 for testing
        points[i] = Point(1, 1, 1)

        j = 0
        while j < i:
            # If any of the coordinates are the same as the any of the previous points
            if (points[i].x != points[j].x) and (points[i].y != points[j].y) and (points[i].z != points[j].z):
                # Do nothing and check next point
                j += 1
            # If some values ARE the same
            else:
                # Start the 2nd loop over and generate a new point and check again
                j = 0
                points[i] = Point()

        i += 1

        # For debugging
        # print('point x: ', point.x)
        # print('point y: ', point.y)
        # print('point z: ', point.z)
        # print('\\')


generate()