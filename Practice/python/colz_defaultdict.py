
from collections import defaultdict
'''
The default factory is called without arguments to produce
a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were
passed to the dict constructor, including keyword arguments.
'''

d = defaultdict()
d["name"] = "narasimha"
d["age"] = 26
print d

d = defaultdict(lambda:"default value")
d["name"] = "narasimha"
d["age"] = 26

print d["name"]
print d["age"]
print d["height"]#instead of giving key error it shows "default value"

s =[('blue',1),('green',2),('red',3),('blue',4),('red',5)]
d= defaultdict(list)
for k,v in s:
    d[k].append(v)
    
print d.items()
    