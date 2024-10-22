import numpy as np
#careful of identical points; ensure that the new point is unique every time you add it
    # Done in generatePoints.py

class Point(object):
    def __init__(self, x: float=None, y: float=None, z: float=None, vel: tuple[float,float,float]=None) -> None:
        self.x = x if x is not None else np.random.random()
        self.y = y if y is not None else np.random.random()
        self.z = z if z is not None else np.random.random()
        self.vel = vel if vel is not None else [np.random.random(), np.random.random(), np.random.random()]

        self.velx = vel[0]
        self.vely = vel[1]
        self.velz = vel[2]