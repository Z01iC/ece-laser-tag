from gpio import isTrigger
from gpio import fireAction
import threading
from time import sleep
from params import *


class fireThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.active = True

	def run(self):
		print('fire   : starting')
		while self.active:
			if isTrigger():
				print('fire   : firing')
				fireAction()
				sleep(trigger_reset_time)
			else:
				sleep(trigger_check_time)

	def kill(self):
		self.active = False


