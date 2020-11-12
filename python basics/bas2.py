f = open("read.txt" , "r+")
for i in range(900,10000):
    i = i+1
    i = str(i)
    comp = f.write("{}\n".format(i))
a = f.read()
print(a)