#!/usr/bin/env python
#  A program that quizes you on the times table
#  -Shriram Krishnamachari 8/17/16


from lifxlan import *
import sys
from time import sleep
from random import randint

lifx = LifxLAN(1)
devices = lifx.get_lights()
bulb = devices[0]

h,s,b,k = bulb.get_color()

for i in range(10):
	bulb.set_color(WARM_WHITE)

	numb1 = (randint(1,10))
	numb2 = (randint(1,10))
	realans = numb1*numb2
	ans = input('What is the answer to '+str(numb1) +'x' +str(numb2) + ': ') 
	if ans == realans:
		bulb.set_color(GREEN)
	else:
		bulb.set_color(RED)
	sleep(2)

bulb.set_color(WARM_WHITE)
