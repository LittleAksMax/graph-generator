import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL_accelerate import *

from constants import *

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
    gluPerspective(100, WIDTH//HEIGHT, Z_MIN_CLIP, Z_MAX_CLIP) # FOV (deg), aspect ratio (width/height), clipping ranges
                                         # at what distances between z co-ordinates do you start and stop seeing an object  
    x = X_DEFAULT
    y = Y_DEFAULT
    z = Z_DEFAULT
    move = 5
    scroll = 10

    glTranslatef(x, y, z) # x, y, z movement
    #glRotatef(0, 0, 0, 0) # deg, x, y, z 
    run = True
    while run:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear slate between flames

        #glGetDoublev(GL_MODELVIEW_MATRIX)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    z += scroll
                    glTranslatef(0, 0, scroll)
                elif event.button == 5:
                    z -= scroll
                    glTranslatef(0, 0, -1 * scroll)
        
        #for i in range(len(edges)): # same as len(vertices) and len(Node.nodes)
        #    p1 = (vertices[edges[i][0]][0], vertices[edges[i][0]][1])
        #    p2 = (vertices[edges[i][1]][0], vertices[edges[i][1]][1])
        #    pygame.draw.line(win, WHITE, p1, p2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x += move
            glTranslatef(move, 0, 0)
        if keys[pygame.K_UP]:
            y -= move
            glTranslatef(0, -1 * move, 0)
        if keys[pygame.K_DOWN]:
            y += move
            glTranslatef(0, move, 0)
        if keys[pygame.K_RIGHT]:
            x -= move
            glTranslatef(-1 * move, 0, 0)
        if keys[pygame.K_RETURN]: # Enter
            # reset co-ordinates
            glTranslatef(X_DEFAULT - x, Y_DEFAULT - y, Z_DEFAULT - z)
            x = X_DEFAULT
            y = Y_DEFAULT
            z = Z_DEFAULT

        drawLines(vertices, edges)

        pygame.display.flip()
        pygame.time.wait(10) # 10ms per frame