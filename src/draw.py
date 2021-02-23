import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL_accelerate import *

from constants import *
from math import *

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
    
    for node in nodes:
        glBegin(GL_POLYGON)
        for i in range(100):    
            cosine = CIRCLE_RADIUS * cos(i * 2 * pi / CIRCLE_SIDES) + node.pos.x    
            sine = CIRCLE_RADIUS * sin(i * 2 * pi / CIRCLE_SIDES) + node.pos.y    
            glVertex2f(cosine, sine)
        glEnd()

# probably going to use multiprocessing so the console can run alongside it
def visualize(vertices, edges, nodes):
    win = create_window()

    # set up player perspective
    gluPerspective(100, WIDTH//HEIGHT, Z_MIN_CLIP, Z_MAX_CLIP) # FOV (deg), aspect ratio (width/height), clipping ranges
                                         # at what distances between z co-ordinates do you start and stop seeing an object  
    x = X_DEFAULT
    y = Y_DEFAULT
    z = Z_DEFAULT

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
                    z += SCROLL
                    glTranslatef(0, 0, SCROLL)
                elif event.button == 5:
                    z -= SCROLL
                    glTranslatef(0, 0, -1 * SCROLL)
        
        #for i in range(len(edges)): # same as len(vertices) and len(Node.nodes)
        #    p1 = (vertices[edges[i][0]][0], vertices[edges[i][0]][1])
        #    p2 = (vertices[edges[i][1]][0], vertices[edges[i][1]][1])
        #    pygame.draw.line(win, WHITE, p1, p2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x += MOVE
            glTranslatef(MOVE, 0, 0)
        if keys[pygame.K_UP]:
            y -= MOVE
            glTranslatef(0, -1 * MOVE, 0)
        if keys[pygame.K_DOWN]:
            y += MOVE
            glTranslatef(0, MOVE, 0)
        if keys[pygame.K_RIGHT]:
            x -= MOVE
            glTranslatef(-1 * MOVE, 0, 0)
        if keys[pygame.K_RETURN]: # Enter
            # reset co-ordinates
            glTranslatef(X_DEFAULT - x, Y_DEFAULT - y, Z_DEFAULT - z)
            x = X_DEFAULT
            y = Y_DEFAULT
            z = Z_DEFAULT

        drawLines(vertices, edges)
        drawNodes(nodes)

        pygame.display.flip()
        pygame.time.wait(10) # 10ms per frame