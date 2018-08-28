
def name():
    yield "krishna"
    yield "arjun"
    yield "adi"
    
itr = name()
print itr
print next(itr)
print next(itr)
print next(itr)
#print next(itr)

for c in name():
    print c