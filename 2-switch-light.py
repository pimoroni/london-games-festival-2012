# Switches the light attached to GPIO 0 on and off depending on
# whether the microswitch is pressed or released
import time
import RPi.GPIO as GPIO

# setup useful constants for later
LED_ON      = GPIO.LOW								# led "on" state
LED_OFF     = GPIO.HIGH								# led "off" state
GPIO_LED    = 0 									# the GPIO pin that we'll attach our LED to
GPIO_SWITCH = 7										# the GPIO pin we'll attach our microswitch to

# allow us to refer to GPIO pins by assigned number (rather than by position)
GPIO.setmode( GPIO.BCM )

# setup the switch pin for input and to return "True" on a down pulse
GPIO.setup( GPIO_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

# set the LED GPIO pin to output mode
GPIO.setup( GPIO_LED, GPIO.OUT )

while True:
	
	if GPIO.input( GPIO_SWITCH ) == True: 			# was the switch pressed?
		GPIO.output( GPIO_LED, LED_ON )				# turn on the LED
	else:
		GPIO.output( GPIO_LED, LED_OFF )			# turn off the LED