
import pytest

class UserMainCode(object):
    
    @classmethod
    def ReverseCharecters(cls,input1):
        a = input1.lower()
        string1 = a.split()
        lst = []
        for i in range(len(string1)):
            b = string1[i][::-1]
            c = b.capitalize()
            lst.append(c)
        print ' '.join(lst)
             
UserMainCode.ReverseCharecters("Hello World")   
a = UserMainCode()
a.ReverseCharecters("i wrote this programm")    

class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
    
a = MyClass()
print a.method()
print a.classmethod()
print a.staticmethod()
print MyClass.classmethod()
print MyClass.staticmethod()
#print MyClass.method()    # TypeError: unbound method method() must be called with MyClass instance as first argument (got nothing instead)


string = "Krishna"
def revers(inpu):
    rev = ""
    for i in range(1,len(string)+1):
        rev = rev + string[len(string) - i]
        print rev
    print "By using for loop         : "+rev
    
revers(string)
    