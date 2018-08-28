n = input("enter no of rows : ")

for row in range(n+1):
    for col in range(1,row+1):
        print col,
    print ''
    
#o/p
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
for row in range(n,0,-1):
    for col in range(1,row+1):
        print col,
    print ''
# o/p
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print col,
    print ""
    
#o/p    
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

#num = 1
for row in range(n,0,-1):
    for col in range(1,row+1):
        print col,
    print ""
# o/p
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print num,
        num += 1
    print ''
     
#o/p:   
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 