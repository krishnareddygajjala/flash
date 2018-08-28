
di = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}


print di.get(5)
print di.items()
print di.keys()
print di.values()
di.update({1:'b',7:'g'})
print di.has_key(1)
print di.pop(1)

for i,j in di.iteritems():
    print i,j
z = di.fromkeys(di)
print z
print di.viewvalues()
string = 'hi, krishna'
print string.split(',')

