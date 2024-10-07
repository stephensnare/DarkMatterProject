import numpy as np
#careful of identical points; ensure that the new point is unique every time you add it

class Point(object):
    def __init__(self, x: float =np.random.random(), y: float=np.random.random(), z: float=np.random.random()) -> None:
        self.x = x
        self.y = y
        self.z = z