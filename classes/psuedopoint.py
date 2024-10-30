import numpy as np

from classes.point import Point

class PsuedoPoint(Point):
    def __init__(self, x, y, z, m):
        self.x = x
        self.y = y
        self.z = z
        self.m = m
        self.pointPointers = []



    def addPointPointer(self, point: Point):
        self.pointPointers.append(point)


    def points(self):
        return self.pointPointers
