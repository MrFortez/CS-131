import pineworkslabs.RPi as GPIO
from time import sleep

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

led = 6
button = 20

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while (True):
	if (GPIO.input(button) == GPIO.HIGH):
		print("hello world")
		sleep(0.5)
	else:
		print("")
		sleep(0.5)
