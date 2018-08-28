
for row in range(1,5):
    for col in range(1,8):
        if row ==4 or row+col ==5 or col-row == 3:
            print '*',
        else:
            print " ",
    print ""

#o/p:
#       *       
#     *   *     
#   *       *   
# * * * * * * * 
n = 6
for row in range(1,n+1):
    for col in range(1,2*n):
        if row ==n or row+col ==n+1 or col-row == n-1:
            print '*',
        else:
            print " ",
    print ""
    