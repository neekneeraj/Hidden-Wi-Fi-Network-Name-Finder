import os 
from Tkinter import *


def sel():
	if select.get() == 1:
			os.system("python deauth.py")
			
	if select.get() == 2:
			os.system("python probehandler.py")




root = Tk()
text = Label(root , text = "Select the attack type to crack Hidden network")
text.pack()
 
select  = IntVar()
select1 = Radiobutton(root, text = "Active attack", value =1, variable = select)
select1.pack(anchor = W)

select2 = Radiobutton(root, text = "Passive attack", value= 2, variable = select)
select2.pack(anchor = W)

button = Button(root , text = "crack" ,command = sel)
button.pack()


root.mainloop()
