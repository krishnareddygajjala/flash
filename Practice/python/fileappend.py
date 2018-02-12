fobj = open("sample.txt","a")
fobj.write("this is the sixth line (appended) \n")
print fobj.tell()
fobj.close()
