import decimal

num = input("enter a number : ")
a = num/10
b= num%10
print a,b
print a+b

mylist = [1,7,7,7,3,9,9,9,7,9,10,0] 
print sorted(set([i for i in mylist if mylist.count(i)>2]))

print bin(num)

def deci_to_bin(n):
    if n>1:
        deci_to_bin(n//2)
    print(n%2),
    
deci_to_bin(num)

def bin_to_dec(n):
    decimal = 0
    for digit in n:
        decimal = decimal*2 + int(digit)
    
    print decimal
bin_to_dec('1100')