# this file is for global variables
from constants import *

def init():
    global console
    global nodesLabelled
    global vertices, edges, nodes
    vertices = []
    edges = []
    nodes = []
    console = None # variable holding ref to console
    nodesLabelled = [False, False] # array with start, end nodes respectively, showing whether they have been labelled