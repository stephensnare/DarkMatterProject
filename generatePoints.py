import numpy as np
from classes.point import Point


def main():
    numPoints = 5
    # 0 to not print coords of each point
    # 1 to print coords of each point
        # DO NOT USE FOR LARGE VALES OF NUMPOINTS
    debug = 0
    generate(numPoints, debug)


def generate(numPoints, debug=0):
    points = np.empty(numPoints, dtype=object)

    i = 0
    while i < numPoints:
        # Creates a new point
        # Currently 1, 1, 1 for testing
        points[i] = Point(1.0, 1.0, 1.0)

        j = 0
        while j < i:
            # print(j)
            # If any of the coordinates are the same as the any of the previous points
            if (points[i].x != points[j].x) and (points[i].y != points[j].y) and (points[i].z != points[j].z):
                # Do nothing and compare next point
                j += 1
            # If some values ARE the same
            else:
                # Start the 2nd loop over, generate a new point and compare again
                j = 0
                points[i] = Point()
                # print(points[i].x)

        # For debugging
        if debug == 1:
            print(f'points[{i}].x: ',points[i].x)
            print(f'points[{i}].y: ',points[i].y)
            print(f'points[{i}].z: ',points[i].z)

        i += 1

main()