import numpy as np
#careful of identical points; ensure that the new point is unique every time you add it
    # Done in generatePoints.py

class Point(object):
    def __init__(self, x: float, y: float, z: float, vel: tuple[float,float,float]) -> None:
        self.x = x 
        self.y = y
        self.z = z

        self.velx = vel[0]
        self.vely = vel[1]
        self.velz = vel[2]

        self.velmag = np.sqrt(self.velx**2 + self.vely**2 + self.velz**2)