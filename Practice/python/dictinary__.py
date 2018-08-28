

det = {1:'a',2:'b',3:'c'}
det1 = {4:'d',5:'e',6:'f'}
print cmp(det, det1)
print det
print det[2]
print det.get(2)
print det.get(4)
print det.keys()
print det.values()
print det.items()
print det.has_key(3)
print det.pop(3)
det.update(det1)
print det.popitem()
print det.popitem()
print det.viewkeys()
print det.viewvalues()
print det.viewitems()

for i in det.iteritems():
    print i
for i in det.iterkeys():
    print i
for i in det.itervalues():
    print i

