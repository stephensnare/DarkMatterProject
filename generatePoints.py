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
        points[i] = Point(None, None, None, [0, 0, 0])

        # For debugging
        if debug == 1:
            print(f'points[{i}].x: ',points[i].x)
            print(f'points[{i}].y: ',points[i].y)
            print(f'points[{i}].z: ',points[i].z)
            print(f'points[{i}].vel: ', points[i].vel)

        i += 1

    return points

main()