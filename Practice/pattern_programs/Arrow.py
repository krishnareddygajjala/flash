
num = int(raw_input("enter no of rows :  "))

for i in range(num):
    for j in range(i):
        print '*',
    print''

for i in range(num,0,-1):
    for j in range(i):
        print '*',
    print ''