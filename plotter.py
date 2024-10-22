import generatePoints as gp
from classes import *
from classes.node import Node
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


### 3D Plotting ###
def plot(points, node):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in points:
        ax.scatter(i.x, i.y, i.z, color='C1')

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    plt.show()