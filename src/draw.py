import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)

def create_window():
    win = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
                                                                     
    pygame.display.set_caption("Visualizer")
    return win

def drawLines(vertices, edges):
    glBegin(GL_LINES) # specify what to draw

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd() 

def drawNodes(nodes):
    glBegin()
    glEnd()

# probably going to use multiprocessing so the console can run alongside it
def visualize(vertices, edges):
    win = create_window()

    # set up player perspective
    gluPerspective(100, WIDTH//HEIGHT, 0.1, 400) # FOV (deg), aspect ratio (width/height), clipping ranges
                                         # at what distances between z co-ordinates do you start and stop seeing an object
    
    glTranslatef(0, 0, -325) # x, y, z movement
    #glRotatef(0, 0, 0, 0) # deg, x, y, z 

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #for i in range(len(edges)): # same as len(vertices) and len(Node.nodes)
        #    p1 = (vertices[edges[i][0]][0], vertices[edges[i][0]][1])
        #    p2 = (vertices[edges[i][1]][0], vertices[edges[i][1]][1])
        #    pygame.draw.line(win, WHITE, p1, p2)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear slate between flames

        drawLines(vertices, edges)

        pygame.display.flip()
        pygame.time.wait(10) # 10ms per frame