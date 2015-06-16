import os 
import time
i = 1
s=['0']
file = open("terminate.txt" , "w")
file.write("0")
file.close()

 

key = " wlan0 "
arg = "iwconfig" + key + " channel "
 
while s[0]=='0':
	file = open("terminate.txt" , "r") 
	s = file.readlines()
	print s
	file.close()
	if i<15:
        
		channel = arg + " %d"%i
		os.system(channel)
		print channel
		i=i+1
 		time.sleep(0.1)	
	else:
		i=1
