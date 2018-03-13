num = str(input("enter a number :"))
rev = str(num[::-1])

if num == rev:
    print "%s is palindrome "%num
else:
    print "%s is not palindrome "%num
    
string = str(raw_input("enter a string :"))
rev = str(string[::-1])
print rev

if string == rev:
    print "%s is palindrome "%string
else:
    print "%s is not palindrome "%string