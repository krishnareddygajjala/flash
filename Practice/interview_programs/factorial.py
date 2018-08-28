def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)

n = input("enter a number : ")

print factorial(n)