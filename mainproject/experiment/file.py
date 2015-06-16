import os 
import threading

file = open("terminate.txt", "w")
file.write("0")
file.close()

file = open("terminate.txt", "r+")
str = file.readlines()
print str
file.truncate(0)	
file.close()

file = open("terminate.txt", "a")
file.write("1")
#str1 =  file.readlines()
#print str1
file.close()

file = open("terminate.txt", "r")
str =  file.readlines()
print str
file.close()

file = open("terminate.txt", "a")
file.write("2")
#str =  file.readlines()
#print str
file.close()
 
file = open("terminate.txt", "r")

str =  file.readlines()
print str
file.close()






#def channel():
#t1= threading.Thread(target=interface)
#t1.start()
#t2= threading.Thread(target=channel)
#t2.start()
