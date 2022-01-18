import agent
import time
import math

def distance(a, b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

class schedular:
	def __init__(self, n=1):
		self.n = n
		self.agent = []
		self.add_agent(n)
		self.agent[0].delivered = True

	def add_agent(self, n=1):
		for i in range(n):
			self.agent.append(agent.agent())

	def move(self):
		for i in range(self.n):
			self.agent[i].move()
		for i in range(self.n):
			if not self.agent[i].delivered:
				continue
			for j in range(self.n):
				if self.agent[j].delivered:
					continue
				if i == j:
					continue
				if distance(self.agent[i].pos, self.agent[j].pos) <= min(self.agent[i].range, self.agent[j].range):
					self.agent[j].delivered = True
