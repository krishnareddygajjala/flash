
def fibo(num):
    if (num<=1):
        return num
    else:
        return (fibo(num-1) + fibo(num-2))

num = int(input("enter a number of terms : "))
print " Fibonacci sequence"
for i in range(num):
    print fibo(i)