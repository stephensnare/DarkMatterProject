from classes.point import Point
## Careful of boundary cases; probably just do a coin flip to choose the side it falls on

class Node(object):
    def __init__(self, side_length: float, center: tuple[float,float,float], depth: int = 1):
        self.side_length = side_length
        self.depth = depth
        self.center = center
        self.population = 0
        self.point: Point or None = None


        # Define children nodes with default values as None
        self.tlf: 'Node' = None  # Top-Left-Front child
        self.trf: 'Node' = None  # Top-Right-Front child
        self.tlb: 'Node' = None  # Top-Left-Back child
        self.trb: 'Node' = None  # Top-Right-Back child
        self.blf: 'Node' = None  # Bottom-Left-Front child
        self.brf: 'Node' = None  # Bottom-Right-Front child
        self.blb: 'Node' = None  # Bottom-Left-Back child
        self.brb: 'Node' = None  # Bottom-Right-Back child


        def split():
            self.trf = Node(self.side_length/2, ((self.center[0]*2)+1, (self.center[1]*2)+1, (self.center[2]*2)+1), self.depth + 1)
            self.tlf = Node(self.side_length/2, ((self.center[0]*2)+1, (self.center[1]*2)-1, (self.center[2]*2)+1), self.depth + 1)
            self.blf = Node(self.side_length/2, ((self.center[0]*2)-1, (self.center[1]*2)-1, (self.center[2]*2)+1), self.depth + 1)
            self.brf = Node(self.side_length/2, ((self.center[0]*2)-1, (self.center[1]*2)+1, (self.center[2]*2)+1), self.depth + 1)
            self.trb = Node(self.side_length/2, ((self.center[0]*2)+1, (self.center[1]*2)+1, (self.center[2]*2)-1), self.depth + 1)
            self.tlb = Node(self.side_length/2, ((self.center[0]*2)+1, (self.center[1]*2)-1, (self.center[2]*2)-1), self.depth + 1)
            self.blb = Node(self.side_length/2, ((self.center[0]*2)-1, (self.center[1]*2)-1, (self.center[2]*2)-1), self.depth + 1)
            self.brb = Node(self.side_length/2, ((self.center[0]*2)-1, (self.center[1]*2)+1, (self.center[2]*2)-1), self.depth + 1)


    def place_point(self, point: Point):
        if point.x<self.center[0]*2**self.depth and point.y<self.center[1]*2**self.depth and point.z<self.center[2]*2**self.depth:
            self.blb.add_point(point)
        if point.x>self.center[0]*2**self.depth and point.y<self.center[1]*2**self.depth and point.z<self.center[2]*2**self.depth:
            self.tlb.add_point(point)
        if point.x<self.center[0]*2**self.depth and point.y>self.center[1]*2**self.depth and point.z<self.center[2]*2**self.depth:
            self.brb.add_point(point)
        if point.x>self.center[0]*2**self.depth and point.y>self.center[1]*2**self.depth and point.z<self.center[2]*2**self.depth:
            self.trb.add_point(point)
        if point.x<self.center[0]*2**self.depth and point.y<self.center[1]*2**self.depth and point.z>self.center[2]*2**self.depth:
            self.blf.add_point(point)
        if point.x<self.center[0]*2**self.depth and point.y>self.center[1]*2**self.depth and point.z>self.center[2]*2**self.depth:
            self.brf.add_point(point)
        if point.x>self.center[0]*2**self.depth and point.y>self.center[1]*2**self.depth and point.z>self.center[2]*2**self.depth:
            self.trf.add_point(point)
        if point.x>self.center[0]*2**self.depth and point.y<self.center[1]*2**self.depth and point.z>self.center[2]*2**self.depth:
            self.tlf.add_point(point)


    def add_point(self, point):
        if self.population == 0:
            self.point = point
            self.population += 1
        elif self.population == 1:
            point1 = point
            point2 = self.point
            self.split()









