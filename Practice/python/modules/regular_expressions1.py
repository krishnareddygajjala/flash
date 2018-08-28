
import re

string = 'abcdacbdlnsnlan'
string1 = "1001 1000 6555 5666 9989 99999 "
s = re.search(r'a', string)
s1= re.search(r'a|l', string) # a or l
print s,s1
print s.group(),s1.group()
print s.group(0)
print re.findall(r'\w', string)
# \w = it matches all alpha-numeric characters [a-zA-Z0-9_] and does not matches special characters
#\W = it matches everything that is not included in [a-zA-Z0-9_]
#Quantifires
# '+' = 1 or more
# '?' = 0 or 1
# '*' = 0 or more
# '{n,m} = n to m repetitions {,3}, {3,}
# '.' = the dot matches any character except the newline
# groups allows us to pull put sections of a match and store them
sm = re.findall(r"\b[5-9][1-9]{3}\b", string1)
print sm

text = open(r"C:\Users\Ram\git\flash\Practice\python\modules\data123.txt","r") 
data = text.read()
text.close()
print data

mail = re.compile(r"[\w.-]+@[\w.-]+\w+?\w+") #johnny_carpenter@smith-dunlap.co.in
d = re.findall(mail, data)
print len(d),d

text1 = open(r"C:\Users\Ram\Desktop\xpath.txt",'r')
dat = text1.read()
text1.close()
print dat