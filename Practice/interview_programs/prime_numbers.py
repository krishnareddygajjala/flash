
def prime_number(value,value1):
    for num in range(value,value1):
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print num
                

value = input("enter a range of values : ")
value1 = input("enter a range of values : ")
prime_number(value,value1)
