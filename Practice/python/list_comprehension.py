squares = []
for x in range(10):
    squares.append(x**2)
print squares
#list comprehension
evensquares1 = [x**2 for x in range(10) if x%2 != 0]
print evensquares1

seq = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]   # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print seq
