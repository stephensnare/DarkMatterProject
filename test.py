# Useful git terminal commands
    # Pushing to master branch on GitHub in the terminal
        # git add .
        # git commit -m "Enter a commit message"
        # git push

    # Pulling from GitHub
        # Make fresh terminal (?)
        # git pull

    # Restore file to previous save state
        # git restore [filepath to the file you want to restore]

import generatePoints as gp
from classes import *
from classes.node import Node

points = gp.generate(30,1)

node = Node(1,(1,1,1),1)

for i in range(len(points)):
    print(i)
    point = points[i]
    node.add_point(point)