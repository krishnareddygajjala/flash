
from collections import deque
'''
deque is list like container with fast append and pop on either end
it is an ordered collection with optimized access from its endpoints.
'''
dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)

print dq
dq.appendleft(6)
dq.appendleft(7)
dq.appendleft(8)
print dq
dq.extend("abc")
print dq
dq.extendleft("xyz")
print dq
dq.pop()
print dq
dq.popleft()
print dq
dq.remove("y")
print dq
dq.clear()
print dq
 


