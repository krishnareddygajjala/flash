l = [1,2,3,12,11,13,14,13,4,14,4,3,11,2,1,5,6,4,6,7,10,8,9,5,4]
al = []
for i in l:
    if i not in al:
        al.append(i)
 
print "removed duplicates using set()         :",list(set(l))       
print "removed duplicates without using set() :" ,al

string = raw_input("enter a string: " )

print "removed duplicates using set()         :","".join(set(string))

astr = []
for i in string:
    if i not in astr:
        astr.append(i)
        
print 'removed duplicates without using set() :',''.join(astr)