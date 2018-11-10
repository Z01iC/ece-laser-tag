from gpio import isHit
from gpio import hitAction
from gpio import displayLives
import threading
from time import sleep
from params import *


class healthThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.lives = max_lives
		self.active = True
		displayLives(self.lives)

	def run(self):
		print('health : starting')
		while self.lives > 0 and self.active:
			if isHit():
				hitAction()
				print('health : hit')
				self.lives = self.lives - 1
				displayLives(self.lives)
				sleep(hit_immunity_time)
			else:
				sleep(hit_check_time)
		print('health : out of lives')

	def kill(self):
		self.active = False


