
import re

text = '''
name,age,salary,mobile,email
lokesh,30,1234567890,+91-9876543210,lokesh.ap@gmail.com
rahul,40,2345678910,+91 8765432190,rahul@gmail.com
cbn,65,3456789120,+917654321980,cbn@outlook.com
jagan,40,4567891230,6543219870,jagan@yahoo.com
pk,40,0123456789,6432109876,pspk_ap@reddif.co.in

00-0C-F1-56-98-AD
00:0a:95:9d:68:16
55:A8:99:66:77:11
98-75-64-52-48-21
01:98:DF:9E:10:37


'''
s ='welcome to python'
string = "krishna.123@ap"

mails =r"\w+\.?\w+?@\w+\.\w+"
mails1 =r"\w+\.?\w+@\w+\.\w+\.?\w+"
mails2 = r'[A-Za-z0-9._]+@\w+\.\w+\.?\w+'
mac = r"[0-9A-Fa-f-:]{17}"

ind_mobile = r'[\+91-]+? ?[6789]\d{9}'
mobile = r'[6789]\d{9}'
name = r'\w+'

mail = re.findall( mails, text) 
mail1 = re.findall( mails1, text)
mail2 = re.findall( mails2, text)#re.findall() function pulls out all the instances from the string 
print "mails :  "+str(mail)
print "mails :  "+str(mail1)
print "mails :  "+str(mail2)
maill = re.search(mails1, text)
print maill.group()

matchobj = re.match(r"welcome", s) #re.match function returns a match object on success, None on failure. it searches only beginning of the string 
if matchobj:
    print "match found "+matchobj.group()
print matchobj.group() #group() = This method returns all matching subgroups in a tuple

mtch = re.match(r"python",s)  #print mtch.group() #this will throw an error

mobile = re.findall(r'[6789]\d{9}', text)
print "mobiles:  "+str(mobile)

replace = re.sub(r"python","bangalore",s)
print replace
replace1 = re.subn(r"a","b","a a a a a a a a")
print replace1

mtch1 = re.search(r"python", s)#re.search function searches anywhere with in the string, only pulls out first instance
print mtch1.group()

rp = re.findall(r'ab+', "abbbbbbb")
print rp

m = re.compile(r"\w+\.?\w+@\w+\.\w+\.?\w+")
for match in m.finditer(text):
    print match.group()

stri = "Narasimha"
for i in re.finditer("a", stri):
    loctup = i.span()
print (loctup)

spl = re.split(m, text)
for i in spl:
    print i
a = re.split('a', "venkata")
print a

v= re.sub('a', 'b', "venkata a a a  ")
print v

v= re.subn('a', 'b', "venkata a a a")
print v

a = "venkata".split("a")
print a

esc = re.escape("pspk_ap@reddif.co.in")
print esc

c = re.search(r"pspk\_ap\@reddif\.co\.in", text)
print c.group()

mac_add = re.findall(mac, text)
print mac_add
indmob = re.findall(ind_mobile, text)
print indmob


