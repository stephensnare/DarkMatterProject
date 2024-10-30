from classes.node import Node
from classes.point import Point
import testFunc


def depthFirstIterative(node, nodesAll):
    if node is None:
        return
    
    nodesAll.append(node.depth)


    depthFirstIterative(node.tlf, nodesAll)
    depthFirstIterative(node.trf, nodesAll)
    depthFirstIterative(node.tlb, nodesAll)
    depthFirstIterative(node.trb, nodesAll)
    depthFirstIterative(node.blf, nodesAll)
    depthFirstIterative(node.brf, nodesAll)
    depthFirstIterative(node.blb, nodesAll)
    depthFirstIterative(node.brb, nodesAll)

    return nodesAll


def depthFirst():
    points, node = testFunc.createAndPlace()
    nodesAll = depthFirstIterative(node, [])
    deepestNode = max(nodesAll)

    return nodesAll, deepestNode