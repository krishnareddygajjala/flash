import os
from subprocess import Popen,PIPE

command = r"ipconfig"

print '******************* subprocess module *******************'
def run_local_command(cmd):
    try:
        proc = Popen(cmd,stdout=PIPE,stderr=PIPE)
        result,error = proc.communicate()
        return result,error
    except Exception,error:
        return "    ",error
    
res,err = run_local_command(command)
print res
print err

print '******************* os module *******************'

def run_command(cmd):
    f = os.popen(cmd)
    data = f.read()
    f.close()
    return data

resu = run_command(command)
print resu
