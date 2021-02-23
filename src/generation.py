from constants import WIDTH, HEIGHT
from node import Node
from random import randint, uniform
from draw import visualize

from multiprocessing import Process # for visualization
processes = []

vertices = []
edges = []

startNodeLabelled = False
endNodeLabelled = False

def generate(nodeCount, edgeCount):
    vertices = [] # empty out vertices
    edges = [] # empty out edges
    Node.nodes = []

    if not nodeCount <= 1: # nodeCount is 0, there is a ZeroDivisionError when calculating p
        # p is probability threshold
        # explanation in README.md
        p = (2 * edgeCount) / (nodeCount * (nodeCount - 1))
        
        for i in range(nodeCount):
            x = randint(-1 * (WIDTH / 2), WIDTH / 2)
            y = randint(-1 * (HEIGHT / 2), HEIGHT / 2)
            vertices.append((x, y, 0)) # 0 z-coordinate
            Node.nodes.append(Node(x, y))

        # for optimization purposes, I will go through and join up as I go
        # rather then add all the links, and then delete the ones that don't
        # meet the threshold   
        for i in range(0, nodeCount - 1):
            for j in range(1, nodeCount):
                if not uniform(0, 1) < p: # doesn't meet threshold
                    continue
                edges.append((i, j))
    
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes
    p = Process(target=visualize, args=[vertices, edges, Node.nodes])
    p.start()
    processes.append(p)
    #visualize(vertices, edges)