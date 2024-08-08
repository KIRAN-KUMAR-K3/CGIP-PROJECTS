import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Automated Rubik's Cube")

glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display_width / display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
], dtype=np.float32)

faces = np.array([
    [0, 1, 2, 3],   
    [3, 2, 6, 7],  
    [7, 6, 5, 4],   
    [4, 5, 1, 0],  
    [1, 5, 6, 2],   
    [4, 0, 3, 7]    
], dtype=np.uint32)

colors = [
    (1, 0, 0),    
    (0, 1, 0),    
    (0, 0, 1),    
    (1, 1, 0),    
    (1, 0.5, 0),  
    (1, 1, 1)     
]

running = True
angle_x = 0
angle_y = 0
angle_z = 0
rotation_speed = 1.0  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)

    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    angle_x += rotation_speed
    angle_y += rotation_speed
    angle_z += rotation_speed

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
