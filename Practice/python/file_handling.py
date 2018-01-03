fobj = open("file.txt")
data = fobj.readlines()
fobj.close()
print "age <= 25 years candidates details: "
for x in data[1:]:
    lst = x.split(",")
    if(int(lst[1]))<=26:
        print "name = ",lst[0]
        print "email= ",lst[-2]
  
print "salary <=50000 candidates details: "
for x in data[1:]:
    lst = x.split(",")
    if(int(lst[2]))<=50000:
        print "name = ",lst[0]
        print "email= ",lst[-2]  
          
print "candidates belong to south india details: "
st = 'south_india'
for x in data[1:]:
    lst = x.split(",")
    if (str(lst[-2])) == st :
        print "name = ",lst[0]
        print "email= ",lst[-3] 
