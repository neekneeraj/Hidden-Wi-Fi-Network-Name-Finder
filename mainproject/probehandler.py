from scapy.all import *
from Tkinter import *
import os 

file = open("info.txt" , "r")
a = file.readlines()
file.close()


t = True
name = []

def probe_response_handler(frame):
					if frame.haslayer(Dot11):
						if frame.addr2 == str(a[0]):
							if frame.type == 0 and frame.subtype == 5:
									print "the SSID of hidden network is %s" %(frame.info)
									name.append(frame.info)	
									global t
									t = False
									os.system("python managedmode.py")
while t:
	sniff(iface= "wlan0" , prn = probe_response_handler, count= 1) 


root = Tk()
text1 = Label(root , text = "Happy Hunting\n")
text1.pack()
text2 = Label(root , text = "The SSID of Hidden Network is " +str(name[0]))
text2.pack()

root.mainloop()