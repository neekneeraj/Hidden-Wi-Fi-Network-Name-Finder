from Tkinter import *
import os


def crack():
	os.system("python monitor.py")
	os.system("python apfinder.py")

def secure():
	os.system("python monitor.py")
	os.system("python newapfinder.py")
	
root = Tk()

frame = Frame(root)
button1 = Button (frame , text = "Crack Hidden Network SSID" ,command = lambda list=list: crack())
button2 = Button (frame , text = "Secure Hidden Network" ,command = lambda list=list: secure())

frame.pack()
button1.pack()
button2.pack()
root.mainloop()
