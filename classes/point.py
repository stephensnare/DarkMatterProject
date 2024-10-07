import numpy as np

class Point():
    def __init__(self, x: float=np.random.random(), y: float=np.random.random(), z: float=np.random.random()) -> None:
        self.x = x
        self.y = y
        self.z = z