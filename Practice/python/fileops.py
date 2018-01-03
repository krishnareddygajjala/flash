def readfile(filename):
    fobj = open(filename)
    data = fobj.read()
    fobj.close()
    return data

data1 = readfile("sample.txt")
print data1,
#lines = data1
#lines1 = data1.split("\n")
#lines2 = lines[:3]
#print lines,lines1,lines2