from constants import WIDTH, HEIGHT, EDGE_OFFSET
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
    if nodeCount != 0: # nodeCount is 0, there is a ZeroDivisionError when calculating p
        # p is probability threshold
        # explanation in README.md
        p = (2 * edgeCount) / (nodeCount * (nodeCount - 1))
        
        for i in range(nodeCount):
            vertices.append(Node(randint(EDGE_OFFSET, WIDTH - EDGE_OFFSET), \
                randint(EDGE_OFFSET, HEIGHT - EDGE_OFFSET)))

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
    p = Process(target=visualize, args=[vertices, edges])
    p.start()
    processes.append(p)
    #visualize(vertices, edges)