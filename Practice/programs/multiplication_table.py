def table(number):
    for i in range(1,11):
        print "%s * %s = %s"%(number,i,(number*i))

inp = input("enter a number : ")
table(inp)