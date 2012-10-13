# The Ladder Game
# (inspired by https://projects.drogon.net/raspberry-pi/gpio-examples/ladder-game/)

# Copyright (c) 2012 Pimoroni Ltd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import time
import RPi.GPIO as GPIO

# setup constants for use late
LED_ON      = GPIO.LOW								# led "on" state
LED_OFF     = GPIO.HIGH								# led "off" state

GPIO_SWITCH = 7										# microswitch pin
GPIO_LEDS   = [ 0, 1, 4, 17, 21, 22, 10, 9, 11 ] 	# list of the GPIO pins connected to LEDs in display order

MAX_LEVEL 	= 9										# maximum game level

# runs the game
def run_game():	
	level = 1 			# start of level 1
	start = time.time() # reset the clock
	current = LED_OFF	# initially the current level LED is off

	print "Game starting..."

	while True:	# loop forever to keep the game running

		if GPIO.input( GPIO_SWITCH ) == True: # was the switch pressed?

			# are we already on the last level? if so, win!
			if level == MAX_LEVEL:	 			
				win() 												# show win animation
				reset_leds();										# turn off all the LEDs
				print "Game starting..."
				level = 1 											# reset to level 1
			else:
				# was button was pressed while LED was on?
				if current == LED_ON:
					print "Level up!"
					level = level + 1 								# go to next level!
					time.sleep( .5 )								# wait half a second
				else:
					lose()
					print "Game starting..."
					level = 1

	 	# time in seconds per flash based on current level
	 	# time ranges from 1 second to 0.22 seconds
	 	time_per_flash =  1.0  / ( level / 2.0 ) 

	 	# check if it's time to blink the current level LED
	 	if time.time() - start > time_per_flash:
	 	  	current = LED_ON if current == LED_OFF else LED_OFF	# toggle the current level LED value
	 		GPIO.output( GPIO_LEDS[ level - 1 ], current )		# update the LED
	 	 	start = time.time()									# reset the clock


# displays the winning animation
def win():
 	print "We have a winner!"

 	# turn off all the LEDs
 	reset_leds()

 	# do "knight rider" effect
 	for y in range( 0, 10 ):
 		# first light up each LED in squence
 		for gpio_idx in GPIO_LEDS[ 1:: ]:
 			GPIO.output( gpio_idx, LED_ON )
 			time.sleep( .05 )
 			GPIO.output( gpio_idx, LED_OFF )

 		# then do the same in reverse
 		for gpio_idx in GPIO_LEDS[ ::-1 ]:
 			GPIO.output( gpio_idx, LED_ON )
 			time.sleep( .05 )
 			GPIO.output( gpio_idx, LED_OFF )

 	# turn off all the LEDs
 	reset_leds()


# displays the losing animation
def lose():
 	print "Game Over!" 	

	# flash all LEDs on and off
 	for x in range( 0, 25 ):
 		reset_leds()

 		time.sleep( .04 )
 			
 		for gpio_idx in GPIO_LEDS:
 			GPIO.output( gpio_idx, LED_ON )
 			
 		time.sleep( .04 )

 	# turn off all the LEDs
 	reset_leds()


# turns off all the LEDs
def reset_leds():
	# turn off all the LEDs
	for gpio_idx in GPIO_LEDS:
		GPIO.output( gpio_idx, LED_OFF )


# sets up the GPIO mode and pins
def setup_gpio():
	# allow us to refer to GPIO pins by assigned number (rather than by position)
	GPIO.setmode( GPIO.BCM )

	# setup the switch pin for input and to return "True" on a down pulse
	GPIO.setup( GPIO_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

	# set all of the LED GPIO pins to output mode
	for gpio_idx in GPIO_LEDS:
		GPIO.setup( gpio_idx, GPIO.OUT )


# let's go!
setup_gpio()
reset_leds()
run_game()