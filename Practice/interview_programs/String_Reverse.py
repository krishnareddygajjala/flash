string = raw_input("enter a string : ")

reverse =''.join(reversed(string))
print "By using join and reversed: "+reverse

print "By using slicing          : "+string[::-1]


def revers(inpu):
    rev = ""
    for i in range(1,len(string)+1):
        rev = rev + string[len(string) - i]
    print "By using for loop         : "+rev
    
revers(string)
print '***** recursive *******'
def reverse(inpu):
    if len(inpu) <= 1:
        return inpu
    return reverse(inpu[1:]) + inpu[0]

print reverse(string)

print '********** Iterative  *********'
def reverse1(inpu):
    return ''.join([inpu[i] for i in range(len(inpu)-1, -1, -1)])

print reverse1(string)

