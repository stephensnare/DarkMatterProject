import numpy as np

class Point(object):
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = np.random.random()
        self.y = np.random.random()
        self.z = np.random.random()