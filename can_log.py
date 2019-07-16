import can
import os
import random

#generating a random number, creating a folder
random_number = random.randint(100,999)

os.makedirs("/home/can_log/%d" % random_number )
file = open("/home/can_log/%d/log.txt" % random_number, "w") 

can_interface = 'can0'
bus = can.interface.Bus(can_interface,bustype='socketcan')

for i in range(10000)
	file.write( "%s" % bus.recv())
	
file.close
