# how to read the conents of a txt file
# f is the file pointer
f = open("amit.txt" , "rt")
content = f.read()
print(content)   #print("6", content)
content = f.read()
print(content) #print("8", content)

f.close()
