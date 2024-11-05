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

    # Plot the points
    for i in points:
        for p in i:
            ax.scatter(p.x, p.y, p.z, color='C1')

    # Draw the cubes
    recursiveDrawCube(node[0], ax)
    recursiveDrawCube(node[1], ax)

    # Set limits and aspect ratio
    ax.set_xlim([0, 1])
    ax.set_ylim([0,1])
    ax.set_zlim([0, 1])
    ax.set_box_aspect([1,1,1])  # Aspect ratio is 1:1:1

    plt.show()


def recursiveDrawCube(node: Node, ax):
    if node.trf is not None:
        recursiveDrawCube(node.trf, ax)
    if node.tlf is not None:
        recursiveDrawCube(node.tlf, ax)
    if node.blf is not None:
        recursiveDrawCube(node.blf, ax)
    if node.brf is not None:
        recursiveDrawCube(node.brf, ax)
    if node.trb is not None:
        recursiveDrawCube(node.trb, ax)
    if node.tlb is not None:
        recursiveDrawCube(node.tlb, ax)
    if node.blb is not None:
        recursiveDrawCube(node.blb, ax)
    if node.brb is not None:
        recursiveDrawCube(node.brb, ax)

    # Draw the cube for the current node
    drawCube(node, ax)


def drawCube(node: Node, ax):
    center = node.center
    side_length = node.side_length

    # Calculate the vertices of the cube
    r = side_length
    cx, cy, cz = center
    cx = cx/(2**node.depth)
    cy = cy/(2**node.depth)
    cz = cz/(2**node.depth)

    # Calculate the vertices of the cube
    points = np.array([[cx - r, cy - r, cz - r],  # 0
                       [cx + r, cy - r, cz - r],  # 1
                       [cx + r, cy + r, cz - r],  # 2
                       [cx - r, cy + r, cz - r],  # 3
                       [cx - r, cy - r, cz + r],  # 4
                       [cx + r, cy - r, cz + r],  # 5
                       [cx + r, cy + r, cz + r],  # 6
                       [cx - r, cy + r, cz + r]])  # 7

    # Define the edges of the cube
    edges = [[points[j] for j in [0, 1, 2, 3, 0]],  # Bottom face
             [points[j] for j in [4, 5, 6, 7, 4]],  # Top face
             [points[j] for j in [0, 4]],  # Vertical edges
             [points[j] for j in [1, 5]],
             [points[j] for j in [2, 6]],
             [points[j] for j in [3, 7]]]

    # Plot the edges
    for edge in edges:
        ax.plot3D(*zip(*edge), color='b')