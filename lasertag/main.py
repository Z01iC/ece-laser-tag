from gpio import isReset
from gpio import resetAction
from gpio import gameOverAction
from gpio import resetGPIO
import health
import fire
from time import sleep
from params import *
from RPi.GPIO import cleanup

try:
	while True:
		resetGPIO()
		resetAction()
		t_health = health.healthThread(1)
		t_fire = fire.fireThread(2)
		t_health.start()
		t_fire.start()
		while True:
			if not t_health.isAlive():
				gameOverAction()
				while not isReset():
					sleep(0.1)
				break
			if isReset():
				break
			sleep(0.05)
		t_health.kill()
		t_fire.kill()
		t_health.join()
		t_fire.join()
		cleanup()

except KeyboardInterrupt:  
	t_health.kill()
	t_fire.kill()
	t_health.join()
	t_fire.join()
    cleanup()       # clean up GPIO on CTRL+C exit  