def square(num):
    return num**2
lst = [1,3,6,5,4,9]

squares = []
for val in lst:
    res = square(val)
    squares.append(res)

print squares

print "***********************************************"

squares1 = map(square,lst)
print squares1