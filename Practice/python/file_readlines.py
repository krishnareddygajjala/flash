def read_lines(filename):
    '''
    read the content of a given file
    '''
    fobj = open(filename,"r")
    data = fobj.readlines()
    fobj.close()
    return data

data1 = read_lines("sample.txt")
#print data1
########################################################
fobj = open("C:\\Users\\Ram\\Desktop\\text.txt","r+")
#print fobj.read()
    
data = fobj.readlines()
i = 1
for line in data:
    #print(str(i)+"."+line),
    i+= 1

#fobj.write("this is the appended line \n")
fobj.close()

with open("C:\\Users\\Ram\\Desktop\\text.txt") as f:
    a = f.readlines()
    print a
    for i in a:
        print i
    f.close()
    