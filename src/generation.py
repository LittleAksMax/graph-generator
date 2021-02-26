from constants import GENERATION_RADIUS
from node import Node
from random import randint, uniform
from draw import visualize
from math import sqrt # for distances

from multiprocessing import Process # for visualization
processes = []

import settings

def distance(node1, node2): # used to determine weights of edges between 2 nodes
    x1, y1 = node1.pos 
    x2, y2 = node2.pos
    return sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def generate(nodeCount, edgeCount):
    settings.vertices = [] # empty out vertices
    settings.edges = [] # empty out edges
    settings.nodes = [] # empty out existing nodes

    if not nodeCount <= 1: # nodeCount is 0, there is a ZeroDivisionError when calculating p
        # p is probability threshold
        # explanation in README.md
        p = (2 * edgeCount) / (nodeCount * (nodeCount - 1))
        
        for i in range(nodeCount):
            x = randint(-1 * (GENERATION_RADIUS / 2), GENERATION_RADIUS / 2)
            y = randint(-1 * (GENERATION_RADIUS / 2), GENERATION_RADIUS / 2)
            settings.vertices.append((x, y, 0)) # 0 z-coordinate
            settings.nodes.append(Node(x, y))

        # for optimization purposes, I will go through and join up as I go
        # rather then add all the links, and then delete the ones that don't
        # meet the threshold   
        for i in range(0, nodeCount - 1):
            node1 = settings.nodes[i]
            for j in range(i + 1, nodeCount):
                if not uniform(0, 1) < p: # doesn't meet threshold
                    continue
                node2 = settings.nodes[j]
                settings.edges.append((i, j))
                node1.neighbors.append(node2)
                node2.neighbors.append(node1)

                weight = distance(node1, node2)

                node1.weights.append(weight)
                node2.weights.append(weight) # should be at the same index as the node appended in neighbors
    
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes
    p = Process(target=visualize, args=[settings.vertices, settings.edges, settings.nodes])
    p.start()
    processes.append(p)