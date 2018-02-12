
fobj = open("C:\\Users\\Ram\\Desktop\\text.txt","r+")
#print fobj.read()
    
data = fobj.readlines()
i = 1
for line in data:
    if line.strip() == "b":
        fobj.write("replaced line")
        
    print(str(i)+"."+line),
    i+= 1
    