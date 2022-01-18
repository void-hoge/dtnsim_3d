import monitor
import schedular
import random

def main():
	random.seed(2)
	schdlr = schedular.schedular(n=10)
	mntr = monitor.monitor()
	while mntr.draw(schdlr):
		schdlr.move()

main()
