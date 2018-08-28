
num = int(raw_input("enter no of rows :  "))

for i in range(0,num):
    for j in range(0,num-i-1):
        print " ",
    for j in range(0,i+1):
        print "* ",
    print ""     
    
def pyramid(rows):
    for i in range(1,rows+1):
        print (' '*(rows-i)+'* '*(i))
pyramid(num)

print "######################"
def reverse_pyramid(rows):
    for i in range(rows,0,-1):
        print (' '*(rows-i)+'* '*(i))
reverse_pyramid(num)


    