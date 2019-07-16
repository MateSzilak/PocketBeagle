import can
import os
import random
import datetime

#generating a random number, creating a folder
random_number = random.randint(100,999)

os.makedirs("/home/can_log/%d" % random_number )
file = open("/home/can_log/%d/log.txt" % random_number, "w") 

can_interface = 'can0'
bus = can.interface.Bus(can_interface,bustype='socketcan')


#adding time&date
now = datetime.datetime.now()    
time_micro = now.strftime('%Y-%m-%d %H:%M:%S.%f') #for the log



for i in range(10000):
	file.write( "time : %s data: %s\n" %(time_micro, bus.recv()))
	
file.close
