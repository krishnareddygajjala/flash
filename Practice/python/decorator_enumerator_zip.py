def deco_func(func):
    def wrap():
        print "wrapper started"
        func()
        print "wrapper ended"
    return wrap

@deco_func
def say():
    print "hello"
    
def say1():
    print "hello 1"

say()
print "##################"
say_hello = deco_func(say1)
say_hello()

lst = range(15)
for i,k in enumerate(lst,1):
    print i,k

lst1 = range(1,11)
lst2 = range(11,21)
print lst1,lst2
z = zip(lst1,lst2)
print z
    
