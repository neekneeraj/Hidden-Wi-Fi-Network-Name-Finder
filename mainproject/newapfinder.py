from scapy.all import *
import threading
from Tkinter import *
import os
import time
import struct
import string

ap_list=[]
ssid = []
channel = []
interface = "wlan0"
t = True
#value = []

def c():
	i = 1
	key = " wlan0 "
	arg = "iwconfig" + key + " channel "  
	global t
	while   t:
		if i<15:
	        
			channel = arg + " %d"%i
			os.system(channel)
			print channel
			i=i+1
	 		time.sleep(0.1)		
		else:
			i=1


def Beacon_Frame_Finder(frame):
	print "Beacon Frame Finder"
	if frame.haslayer(Dot11):
		if frame.type == 0 and frame.subtype == 8:
			if frame.addr2 not in ap_list:
				ap_list.append(frame.addr2)
				a =struct.unpack("B",frame[Dot11Elt:3].info)
				channel.append(a[0])
				print channel
				if (frame.info == '') or (not(all(c in string.printable for c in frame.info))):
					print "AP MAC: %s with SSID: %s" %(frame.addr2, "Hidden Network")
					ssid.append("Hidden Network")
				#if (not(all(c in string.printable for c in frame.info))):
					#print "AP MAC: %s with SSID: %s" %(frame.addr2, "Hidden Network")
					#ssid.append("Hidden Network")
				else:
					print "AP MAC %s with SSID: %s" %(frame.addr2 , frame.info)
					ssid.append(frame.info)


def s():
	global t
	while t:
		sniff(iface = interface , prn = Beacon_Frame_Finder, count = 1) 




def i():
	def delete(): 
		while TRUE:
			print"Hello"
	        	list.delete(0, END)
			#list.insert(END, "MAC Address" + '         ' + "Network Name" + '    '+ "Channel")
	    		for i in range(0, len(ap_list)):
					list.insert(END, ap_list[i]+ '     ' + ssid[i])  
	      		time.sleep(7)
	

	def kill():
		global t
		t = False
		value = map(int, list.curselection())
		#print value[0]
		#print str(channel[value[0]])
		#x=value[0]
		print "managed mode"
		os.system("python managedmode.py")
		os.system("airmon-ng start wlan0")
		str1 = "iwconfig " + interface + " channel " + str(channel[value[0]])
		os.system(str1)
		file = open("info.txt", "w")
		file.write(ap_list[value[0]])
		file.close()
		os.system("python hard.py")
		
		
	
	root = Tk()
	frame = Frame(root)
	list=Listbox(frame, height=20, width=50)
	button1 = Button (frame , text = "Select Network" ,command = lambda list=list: kill())
	label1 = Label(root, text = "MAC address")
	label2 = Label(root, text = "NETWORK NAME")
	label1.pack()
	label1.place(x = 0, y= 0)
	label2.pack()
	frame.pack()
	
	list.pack()
	button1.pack()
	
	list.insert(END, "Select Hidden Network to crack")
	root.title("Choose Network")
	
		
	t4 = threading.Thread(target=delete)							
	t4.start()
	root.mainloop()


t1=threading.Thread(target=s)
t2=threading.Thread(target=c)
t3=threading.Thread(target=i)
t1.start()
t2.start()
t3.start()



