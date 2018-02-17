
from collections import OrderedDict
''' OrderedDict  this is an ordered dictionary
    supports all dict methods
    new methods are popitem()
'''
od = OrderedDict()
od['name'] = 'krishna'
od['age'] = 25
od['salary'] = 50000

print od         #OrderedDict([('name', 'krishna'), ('age', 25), ('salary', 50000)])
print od.items() #[('name', 'krishna'), ('age', 25), ('salary', 50000)]
print od.keys()  #['name', 'age', 'salary']
print od.values()#['krishna', 25, 50000]