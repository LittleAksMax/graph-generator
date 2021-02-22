import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from constants import WIDTH, HEIGHT

def create_window():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Visualizer")
    return win

# probably going to use multiprocessing so the console can run alongside it
def visualize(vertices, edges):
    win = create_window()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()