
import os



#Returns the current working directory.
print os.getcwd()

#Return a unicode string representing the current working directory
print os.getcwdu()

print os.path.abspath('.')
print os.listdir(r'C:\Users\Ram\git\flash\Practice\python\modules')
print os.chdir(r'C:\Users\Ram')
print os.name     # nt for windows
#print os.mkdir(r"C:\Users\Ram\Desktop\dir")
print os.makedirs(r"C:\Users\Ram\Desktop\dir\dir")


