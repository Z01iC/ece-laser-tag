import RPi.GPIO as RGPIO
import threading
from params import *

pwm_emitter = None

def resetGPIO():
	RGPIO.cleanup()

	### RGPIO setup and pinout ###
	RGPIO.setmode(RGPIO.BCM)
	RGPIO.setwarnings(False)

	#emitter
	RGPIO.setup(p_emitter, RGPIO.OUT)
	global pwm_emitter
	pwm_emitter = RGPIO.PWM(p_emitter, emitter_freq)

	#trigger
	RGPIO.setup(p_trigger, RGPIO.IN, pull_up_down=RGPIO.PUD_DOWN)

	#detection
	RGPIO.setup(p_detection, RGPIO.IN, pull_up_down=RGPIO.PUD_DOWN)

	#hit display
	RGPIO.setup(p_hit, RGPIO.OUT)

	#lives
	for i in range(max_lives):
		RGPIO.setup(p_life[i], RGPIO.OUT)

	#feedback buzzer
	RGPIO.setup(p_buzzer, RGPIO.OUT)

	#feedback vibrator
	RGPIO.setup(p_vibrator, RGPIO.OUT)

	#reset
	RGPIO.setup(p_reset, RGPIO.IN, pull_up_down=RGPIO.PUD_DOWN)


### IO abstraction functions ###
def isHit():
	return RGPIO.input(p_detection)

def isTrigger():
	return RGPIO.input(p_trigger)

def isReset():
	return RGPIO.input(p_reset)

def displayLives(lives):
	for i in range(max_lives):
		if lives > i:
			RGPIO.output(p_life[i], RGPIO.HIGH)
		else:
			RGPIO.output(p_life[i], RGPIO.LOW)

def fireAction():
	pwm_emitter.start(emitter_duty_cycle)
	threading.Timer(emitter_duration, pwm_emitter.stop).start()

def hitAction():
	RGPIO.output(p_hit, RGPIO.HIGH)
	threading.Timer(hit_feedback_duration, RGPIO.output, args=(p_hit, RGPIO.LOW)).start()

def resetAction():
	pass

def gameOverAction():
	pass

