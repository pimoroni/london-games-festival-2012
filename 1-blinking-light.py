# Blinks an LED attached to GPIO pin 0

import time
import RPi.GPIO as GPIO

# setup useful constants for later
LED_ON      = GPIO.LOW								# led "on" state
LED_OFF     = GPIO.HIGH								# led "off" state
GPIO_LED    = 0 									# the GPIO pin that we'll attach our LED to

# allow us to refer to GPIO pins by assigned number (rather than by position)
GPIO.setmode( GPIO.BCM )

# set the LED GPIO pin to output mode
GPIO.setup( GPIO_LED, GPIO.OUT )


while True:

	GPIO.output( GPIO_LED, LED_ON )					# turn on the LED
	time.sleep( 0.5 )								# wait for 0.5 seconds

	GPIO.output( GPIO_LED, LED_OFF )				# turn off the LED
	time.sleep( 0.5 )								# wait for 0.5 seconds
