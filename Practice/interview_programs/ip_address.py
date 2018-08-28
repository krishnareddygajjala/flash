
import os
import re
cmd = r"ipconfig"
cmd1 = r"tasklist"
f = os.popen(cmd1)
data = f.read()
f.close()
#print data
ip = re.findall(r"IPv4 Address.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data)
tasklist = re.findall(r"\w+.exe", data)
#print ip
print data
print len(set(tasklist))
print len(tasklist)
