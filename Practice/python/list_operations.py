# list is a co
# methods like insert, remove or sort that only modify the list have no return value printed – they return the default None.
lst = [1,2,3,4,5,6,7,8,9,10,11]
lst2 = [13,14,15,16,17,18,19,20,21,22,23]
print lst
#append = adds value at last of a sequence
lst.append(12)
print lst
#insert = insert value at a desired index
lst.insert(0, 0) 
print lst
#index = index of given value       
print lst.index(5)
#count = no of occurrences of a given value
print lst.count(10)
#extend = adding or merging more than one list
lst2.extend(lst)
print lst2
#remove = remove a value from a sequence
lst.remove(0)
print lst
#pop = by default it removes the last value of a sequence ,if we pass the index as a input of pop it removes the indexed value
lst2.pop() 
print lst2 
lst2.pop(5)
print lst2
#sort = to make list as a ordered list sort(cmp=None, key=None, reverse=False)
lst2.sort() #ascending(default)
print lst2
lst2.sort(cmp=None, key=None, reverse=True) #descending
print lst2
#reverse = just reverses the list
lst3 = [9,9,4,9,2,9,8,4,8,3]
lst3.reverse()
print lst3