
from collections import Counter


'''
it also a part of dict subclass and it is used for counting objects
it is an unordered collection 
where elements are stored as dictionary keys and 
     their counts are stored as dictionary values. 

'''

c = Counter("narasimha")

print c
c = Counter([1,1,1,2,3,3,3,4,5,6,8,8,9,9,9,9])

print c
c = Counter("narasimha")
print list(c.elements())
print c.most_common(3)
print c.keys()