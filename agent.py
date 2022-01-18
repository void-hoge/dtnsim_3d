import random
import math

def add_vec(a, b):
	return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def mul_vec(vec, c):
	return [vec[0]*c, vec[1]*c, vec[2]*c]

class agent:
	def __init__(self):
		self.pos = (random.uniform(-1,1), random.uniform(1,-1), random.uniform(1,-1))
		self.delivered = False
		self.range = 0.15

	def random_vec(self):
		# returns a 3dim vector of length 1.
		theta = random.uniform(0, 2*math.pi)
		p = random.uniform(.0,1.0)
		phi = math.asin(2.0*p-1)
		x = math.cos(phi) * math.cos(theta)
		y = math.cos(phi) * math.sin(theta)
		z = math.sin(phi)
		return [x,y,z]

	def move(self):
		# random walk
		self.pos = add_vec(self.pos, mul_vec(self.random_vec(), random.uniform(0,0.1)))
		if self.pos[0] > 1.0:
			self.pos[0] = 1.0
		if self.pos[0] < -1.0:
			self.pos[0] = -1.0
		if self.pos[1] > 1.0:
			self.pos[1] = 1.0
		if self.pos[1] < -1.0:
			self.pos[1] = -1.0
		if self.pos[2] > 1.0:
			self.pos[2] = 1.0
		if self.pos[2] < -1.0:
			self.pos[2] = -1.0
