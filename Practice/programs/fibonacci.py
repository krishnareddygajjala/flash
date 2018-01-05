#fibonacci series using recursion
def fibonacci(num):
    """a series of numbers in which each number
    ( Fibonacci number ) is the sum of the two preceding numbers.
    The simplest is the series 1, 1, 2, 3, 5, 8, etc."""
    if(num <= 1):
        
        return num     
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))

num = int(input("enter number of terms : "))
print ("fibonacci sequence: ")
#############################################################
for i in range(num):
    print fibonacci(i)
    
#fibonacci series without using recursion 
def fibonacci1(num1):
    a=int(input("Enter the first number of the series "))
    b=int(input("Enter the second number of the series "))
    num1=int(input("Enter the number of terms needed "))
    print(a,b)
    while(num1-2):
        c=a+b
        a=b
        b=c
        print(c)
        num1=num1-1
##########################################################
fibonacci1(10)