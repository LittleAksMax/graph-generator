from status import Status

class Node(object):
    
    def __init__(self, x, y):
        self.pos = (x, y)
        self.neighbors = []
        self.weights = [] # decided by distance

        self.state = Status.Unvisited
    
    def __str__(self):
        return f"({self.pos[0]}, {self.pos[1]})"