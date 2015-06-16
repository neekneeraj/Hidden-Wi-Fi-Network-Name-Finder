import os 

key = " wlan0 "
arg1 = "ifconfig" + key
arg2 = "iwconfig" + key
os.system(arg1 + " down" )
os.system(arg2 + " mode monitor")
os.system(arg1 + " up")
 
