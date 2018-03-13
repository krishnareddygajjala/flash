import os
import re
def run_command(cmd):
    f = os.popen(cmd)
    data = f.read()
    f.close()
    return data

data = run_command(r"tasklist")
lines = data.split("\n")

for line in lines:
    #print line
    
    if "svchost" in line:
        l = line.split()
        #print l[1]
        #os.kill(int(l[1]),9)
        
data1 = run_command(r'ipconfig')
#print data1
ipadd = r'IPv4 Address.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip = re.findall(ipadd,data1)
print ip
print 'the ip address is : '+ip[0].split()[-1]