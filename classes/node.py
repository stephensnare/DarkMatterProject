from classes.point import Point
from classes.psuedopoint import PsuedoPoint


## Careful of boundary cases; probably just do a coin flip to choose the side it falls on

class Node(object):
    def __init__(self, side_length: float, center: tuple[float, float, float], depth: int = 1):
        self.side_length = side_length
        self.depth = depth
        self.center = center
        self.population = 0
        self.point: Point | None = None

        self.psuedoPoint: PsuedoPoint = PsuedoPoint(0, 0, 0, 0)

        self.parent: Node | None = None

        # Define children nodes with default values as None
        self.tlf: 'Node' = None  # Top-Left-Front child
        self.trf: 'Node' = None  # Top-Right-Front child
        self.tlb: 'Node' = None  # Top-Left-Back child
        self.trb: 'Node' = None  # Top-Right-Back child
        self.blf: 'Node' = None  # Bottom-Left-Front child
        self.brf: 'Node' = None  # Bottom-Right-Front child
        self.blb: 'Node' = None  # Bottom-Left-Back child
        self.brb: 'Node' = None  # Bottom-Right-Back child

    def split(self):
        self.trf = Node(self.side_length / 2,
                        ((self.center[0] * 2) + 1, (self.center[1] * 2) + 1, (self.center[2] * 2) + 1), self.depth + 1)
        self.tlf = Node(self.side_length / 2,
                        ((self.center[0] * 2) + 1, (self.center[1] * 2) - 1, (self.center[2] * 2) + 1), self.depth + 1)
        self.blf = Node(self.side_length / 2,
                        ((self.center[0] * 2) - 1, (self.center[1] * 2) - 1, (self.center[2] * 2) + 1), self.depth + 1)
        self.brf = Node(self.side_length / 2,
                        ((self.center[0] * 2) - 1, (self.center[1] * 2) + 1, (self.center[2] * 2) + 1), self.depth + 1)
        self.trb = Node(self.side_length / 2,
                        ((self.center[0] * 2) + 1, (self.center[1] * 2) + 1, (self.center[2] * 2) - 1), self.depth + 1)
        self.tlb = Node(self.side_length / 2,
                        ((self.center[0] * 2) + 1, (self.center[1] * 2) - 1, (self.center[2] * 2) - 1), self.depth + 1)
        self.blb = Node(self.side_length / 2,
                        ((self.center[0] * 2) - 1, (self.center[1] * 2) - 1, (self.center[2] * 2) - 1), self.depth + 1)
        self.brb = Node(self.side_length / 2,
                        ((self.center[0] * 2) - 1, (self.center[1] * 2) + 1, (self.center[2] * 2) - 1), self.depth + 1)

    def place_point(self, point: Point):
        self.psuedoPoint.addPointPointer(point)
        if point.x <= self.center[0] / 2 ** self.depth and point.y <= self.center[1] / 2 ** self.depth and point.z <= \
                self.center[2] / 2 ** self.depth:
            self.blb.add_point(point)
            self.blb.parent = self
        elif point.x >= self.center[0] / 2 ** self.depth and point.y <= self.center[1] / 2 ** self.depth and point.z <= \
                self.center[2] / 2 ** self.depth:
            self.tlb.add_point(point)
            self.tlb.parent = self
        elif point.x <= self.center[0] / 2 ** self.depth and point.y >= self.center[1] / 2 ** self.depth and point.z <= \
                self.center[2] / 2 ** self.depth:
            self.brb.add_point(point)
            self.brb.parent = self
        elif point.x >= self.center[0] / 2 ** self.depth and point.y >= self.center[1] / 2 ** self.depth and point.z <= \
                self.center[2] / 2 ** self.depth:
            self.trb.add_point(point)
            self.trb.parent = self
        elif point.x <= self.center[0] / 2 ** self.depth and point.y <= self.center[1] / 2 ** self.depth and point.z >= \
                self.center[2] / 2 ** self.depth:
            self.blf.add_point(point)
            self.blf.parent = self
        elif point.x <= self.center[0] / 2 ** self.depth and point.y >= self.center[1] / 2 ** self.depth and point.z >= \
                self.center[2] / 2 ** self.depth:
            self.brf.add_point(point)
            self.brf.parent = self
        elif point.x >= self.center[0] / 2 ** self.depth and point.y >= self.center[1] / 2 ** self.depth and point.z >= \
                self.center[2] / 2 ** self.depth:
            self.trf.add_point(point)
            self.trf.parent = self
        elif point.x >= self.center[0] / 2 ** self.depth and point.y <= self.center[1] / 2 ** self.depth and point.z >= \
                self.center[2] / 2 ** self.depth:
            self.tlf.add_point(point)
            self.tlf.parent = self

    def add_point(self, point, debug=0):
        if self.population == 0:
            self.point = point
            if debug == 1:
                print(f"added point at depth = {self.depth}")

        elif self.population == 1:
            point1 = point
            point2 = self.point
            self.split()
            self.point = None
            self.place_point(point1)
            self.place_point(point2)

        else:
            self.place_point(point)

        self.population += 1

    def burn_tree(self):

        if self.blf:
            self.blf.burn_tree()
            self.blf = None
        if self.blb:
            self.blb.burn_tree()
            self.blb = None
        if self.brf:
            self.brf.burn_tree()
            self.brf = None
        if self.brb:
            self.brb.burn_tree()
            self.brb = None
        if self.tlf:
            self.tlf.burn_tree()
            self.tlf = None
        if self.tlb:
            self.tlb.burn_tree()
            self.tlb = None
        if self.trf:
            self.trf.burn_tree()
            self.trf = None
        if self.trb:
            self.trb.burn_tree()
            self.trb = None

    def placePoints(self, points):
        for p in points:
            self.add_point(p)