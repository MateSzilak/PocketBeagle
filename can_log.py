import can
import os
import random

#generating a random number, creating a folder
random_number = random.randint(100,999)

os.makedirs("/home/%d" % random_number )
file = open("/home/%d/log.txt" % random_number, "w") 

can_interface = 'can0'
bus = can.interface.Bus(can_interface,bustype='socketcan')

for i in range(10000):
	file.write( "%s\n" % bus.recv())
	
file.close
