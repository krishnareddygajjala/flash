def intpalindrome():
    value = str(input("enter a value :"))
    rev = str(value)[::-1]
    if value == '0':
        print "enter a positive integer"
    elif value == rev:
        print (value,"is a palindrome")
    else:
        print value,"is not a palindrome"

intpalindrome()

def stringpalindrome():
    string = raw_input("enter a value :")
    print string
    rev = string[::-1]
    if string == '0':
        print "enter a positive integer"
    elif string == rev:
        print (string,"is a palindrome")
    else:
        print string,"is not a palindrome"

stringpalindrome()


