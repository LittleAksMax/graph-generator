from coor import Coor
from status import Status

class Node(object):
    def __init__(self, x, y):
        self.pos = Coor(x, y)
        self.neighbors = []
        self.weights = [] # decided by distance

        self.state = Status.Unvisited