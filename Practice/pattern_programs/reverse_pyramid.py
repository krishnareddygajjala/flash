

num = int(raw_input("enter no of rows :  "))

for i in range(num,0,-1):
    for j in range(0,num-i):
        print "",
    for j in range(0,i):
        print "* ",
    print ""     