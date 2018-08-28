
number = "123"
reverse =''.join(reversed(number))

print "By using slicing          : "+number[::-1]

print "By using join and reversed: "+reverse

rev = ""
for i in range(1,len(number)+1):
    rev = rev + number[len(number) - i]
print "By using for loop         : "+rev

#num = input("enter a number : ")
num = 123
rev =0
while num > 0:
    rev = (rev*10) + num%10
    num //= 10
print rev
    