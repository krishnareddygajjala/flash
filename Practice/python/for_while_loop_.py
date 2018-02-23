persons =['krishna','arjun','narasimha','adi']

print "*************FOR LOOP***************"

for name in persons:
    #print "hi,{}!".format(name)
    print "hi,%s!"%name

print "*************WHILE LOOP***************"

index = 0
while index<len(persons):
    #print "hi,{}!".format(persons[index])
    print "hi!,%s!"%persons[index]
    index +=1