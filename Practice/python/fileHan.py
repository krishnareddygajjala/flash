f = open("foo.txt","wb")
print ("name of the file:",f.name)
print (" file is closed or not:",f.closed)
print ("mode of the file:",f.mode)
f.write("this is dummy text file")
f.close()
'''
output:
('name of the file:', 'foo.txt')
(' file is closed or not:', False)
('mode of the file:', 'wb')
'''