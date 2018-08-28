string = "Krishna"
reverse =''.join(reversed(string))

print "By using slicing           : "+string[::-1]

print "By using join and reversed : "+reverse

def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]

print "By using recursive function: "+reverse(string)


def reverse1(string):
    rev = ''
    for i in range(1,len(string)+1):
        rev = rev + string[len(string) - i]       
    print "By using for loop          : "+rev
    
reverse1(string)
