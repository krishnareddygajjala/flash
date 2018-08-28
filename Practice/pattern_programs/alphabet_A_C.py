print "A"
for row in range(1,5):
    for col in range(1,8):
        if row+col ==5 or col-row == 3 or ((row ==3) and (col>1 and col<7)):
            print '*',
        else:
            print " ",
    print ""
    
print "K"

for row in range(1,8):
    for col in range(1,5):
        if col == 1 or row+ col == 5 or row-col == 3:
            print '*',
        else:
            print " ",
    print ""
    
print "  M  "  
 
for row in range(1,6):
    for col in range(1,6):
        if col==1 or col==5 or (row==col==2) or (row==col==3) or (row==2 and col==4) :
            print '*',
        else:
            print " ",
    print ""
    
    
print " S "
for row in range(1,8):
    for col in range(1,5):   
        if row == 1 or row == 4 or row == 7 or (col==1 and (row >1 and row <4)) or (col == 4 and (row > 4 and row < 7)):
            print "*",
        else :
            print " ",
    print ""