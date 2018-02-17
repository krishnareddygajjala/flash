
from collections import namedtuple

"""Returns a new subclass of tuple with named fields.
 
 """
student = namedtuple('student', ['name','age','rollno'])
student1 = student("akash",21,3)
print "name:",student1.name
print "age:",student1.age
print student1._fields
print student1._replace(name="student name")