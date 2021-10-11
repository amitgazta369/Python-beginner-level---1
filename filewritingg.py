 f = open("amit7.txt", "w")
 f.write("amit gazta is very brilliant\n")
f.close()
# r+ mode is usd for both read nd wriiting
f = open("amit7.txt",("r+"))
print(f.read())
f.write("thankk bhaii jiii")

