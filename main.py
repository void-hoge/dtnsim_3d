#!/usr/bin/env python3
import monitor
import schedular
import random

def main():
	random.seed(2)
	schdlr = schedular.schedular(n=10)
	mntr = monitor.monitor()
	while mntr.draw(schdlr):
		schdlr.move()

if __name__ == '__main__':
	main()
