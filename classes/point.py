import numpy as np
#careful of identical points; ensure that the new point is unique every time you add it
    # Done in generatePoints.py

class Point(object):
    def __init__(self, x: float, y: float, z: float, vel: tuple[float,float,float]) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.vel = vel

        self.velx = vel[0]
        self.vely = vel[1]
        self.velz = vel[2]

        self.velmag = np.sqrt(self.velx**2 + self.vely**2 + self.velz**2)

        self.acc = [0,0,0]


    def update_params(self, dt: float):
        self.x += dt * self.velx + dt**2 * self.acc[0]
        self.y += dt * self.vely + dt**2 * self.acc[1]
        self.z += dt * self.velz + dt**2 * self.acc[2]

        self.velx += dt * self.acc[0]
        self.vely += dt * self.acc[1]
        self.velz += dt * self.acc[2]

        self.vel = [self.velx, self.vely, self.velz]
        
        self.velmag = np.sqrt(self.velx**2 + self.vely**2 + self.velz**2)
