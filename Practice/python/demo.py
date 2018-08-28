
with open(r"C:\Users\Ram\Desktop\imp\text12.txt","r") as f:
    data = f.read()
    print data
if "line" in data:
    print "it is there"
    print data.count("line")
    