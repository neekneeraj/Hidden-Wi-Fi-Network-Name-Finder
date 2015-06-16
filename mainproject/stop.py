file = open("terminate.txt", "r+")
file.truncate(0)	
file.close()

file = open("terminate.txt", "a")
file.write("1")
file.close()