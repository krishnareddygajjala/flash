def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring='qwertyqweryyyy'
count_dict(mystring)

from collections import Counter
print Counter(mystring)