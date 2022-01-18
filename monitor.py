import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import agent
import time

verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
             (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0,1), (0,3), (0,4), (2,1),(2,3), (2,7), (6,3), (6,4),(6,7), (5,1), (5,4), (5,7))

def mul_tuple(t, c):
	return (t[0]*c, t[1]*c, t[2]*c)

class monitor:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.display = (1280, 720)
		pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
		pygame.key.set_repeat(50)
		glEnable(GL_BLEND)
		glEnable(GL_DEPTH_TEST)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		gluPerspective(70, (self.display[0]/self.display[1]), 0.1, 50.0)
		glTranslatef(0.0, 0.0, -10)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION,  (0, 10, 5, 1))
		glEnable(GL_COLOR_MATERIAL)

	def draw_agent(self, ag):
		glTranslatef(ag.pos[0]*3, ag.pos[1]*3, ag.pos[2]*3)
		# core
		if ag.delivered:
			glColor4f(1,0.3,0,1)
		else:
			glColor4f(0,1,0,1)
		glutSolidSphere(ag.range/2, 20, 20)
		# range
		if ag.delivered:
			glColor4f(1,0.3,0,0.5)
		else:
			glColor4f(0,1,0,0.5)
		glutSolidSphere(ag.range*3, 20, 20)
		glTranslatef(-ag.pos[0]*3, -ag.pos[1]*3, -ag.pos[2]*3)

	def rotate(self, a, b):
		glRotatef(1,a,b,0)

	def zoom(self, a):
		glTranslatef(0.0, 0.0, a)

	def draw_wirecube(self):
		glBegin(GL_LINES)
		glColor3f(1,1,1)
		for edge in edges:
			for vertex in edge:
				glVertex3fv(mul_tuple(verticies[vertex],3))
		glEnd()

	def draw(self, schedular):
		self.clock.tick(100)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		for ag in schedular.agent:
			self.draw_agent(ag)
		self.draw_wirecube()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return False
			if event.type == pygame.KEYDOWN:
				if event.key == ord('w'):
					self.rotate(1,0)
				elif event.key == ord('s'):
					self.rotate(-1,0)
				elif event.key == ord('a'):
					self.rotate(0,1)
				elif event.key == ord('d'):
					self.rotate(0,-1)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					self.zoom(1)
				if event.button == 5:
					self.zoom(-1)
		pygame.display.flip()
		return True
