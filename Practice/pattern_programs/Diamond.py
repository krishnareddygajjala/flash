

num = int(raw_input("enter no of rows :  "))

for i in range(0,num):
    for j in range(0,num-i-1):
        print " ",
    for j in range(0,i+1):
        print "* ",
    print ""     

for i in range(num-1,0,-1):
    for j in range(0,num-i):
        print "",
    for j in range(0,i):
        print "* ",
    print "" 
    
    