string = "Krishna Reddy"
reverse =''.join(reversed(string))

print "By using slicing          : "+string[::-1]

print "By using join and reversed: "+reverse

rev = ""
for i in range(1,len(string)+1):
    rev = rev + string[len(string) - i]
print "By using for loop         : "+rev

