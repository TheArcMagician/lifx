#!/usr/bin/env python
from lifxlan import *
import sys
from time import sleep

lifx = LifxLAN(1)
devices = lifx.get_lights()
bulb = devices[0]

h,s,b,k = bulb.get_color()

#bulb.set_color((h,s,b,k))

while True:
	brightness = raw_input("Set brightness to: (low, medium, high) ")

	if brightness == "low":
		bulb.set_color((h,s,10000,k))
	elif brightness == 'medium':
		bulb.set_color((h,s,30000,k))
	elif brightness == 'high':
		bulb.set_color((h,s,60000,k))
	else: 
		print('please select from low, medium or high.')
