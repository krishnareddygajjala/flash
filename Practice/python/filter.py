lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def oddsquare(num):
    if num%2 == 1:
        return num**2

oddsquares = filter(oddsquare,lst)
print oddsquares
odds = []
for val in lst:
    if val%2 == 1:
        odds.append(val)

print odds  
    