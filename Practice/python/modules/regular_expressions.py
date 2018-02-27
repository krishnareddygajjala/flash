
import re


text = '''
name,age,salary,mobile,email
papu,30,1234567890,9876543210,papu.ap@gmail.com
rahul,40,2345678910,8765432190,peddapapu@gmail.com
cbn,65,3456789120,7654321980,cbn@outlook.com
jagan,40,4567891230,6543219870,jagan@yahoo.com
pk,40,0123456789,6432109876,pspk@reddif.co.in
'''
s ='welcome to python'
mails =r"\w+\.?\w+?@\w+\.\w+"
mails1 =r"\w+\.?\w+?@\w+\.\w+\.?\w+"
ind_mobile = r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$'
mobile = r'[6789]\d{9}'

mail = re.findall( mails, text)
print "mails :"+str(mail)
matchobj = re.match(r"welcome", s)
#print matchobj2w1
#print matchobj.group()

mobile = re.findall(r'[6789]\d{9}', text)
print mobile


