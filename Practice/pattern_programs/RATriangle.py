
num = int(raw_input("enter no of rows :  "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print "*",
    print ""
    

for i in range(num+1):
    for j in range(i):
        print '*',
    print''