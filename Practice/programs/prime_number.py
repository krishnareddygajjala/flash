def prime(number):
    if number == 1:
        print "not prime"
    else:
        n = 2
        while n < number:
            if number%2 == 0:
                return "not prime"
            n +=1
        return "prime"
n = input("enter a number : ")
res = prime(n)
print "number %s is "%n,res
print "######################################################"
num = int(input("enter a number : "))

for number in range(2,num):
    if number > 1:
        for i in range(2,number):
            if (number % i == 0):
                break
        else:
            print number,"is a prime number"

    