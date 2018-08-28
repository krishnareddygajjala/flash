def factorial(number):
    '''
    to find a factorial of a given number
    '''
    fact = 1
    while number >1:
        fact = fact*number
        number -= 1
    return fact

n = input("enter a number : ")
res = factorial(n)
print "factorial of %s ="%n,res

fact = reduce(lambda a,b : a*b ,range(1,n+1))
print "factorial of %s ="%n,fact