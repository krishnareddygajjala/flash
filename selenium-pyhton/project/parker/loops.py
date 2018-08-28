
class kri():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def pprint(self,age):
        """it prints your name and age"""
        print self.fname+" "+self.lname+" "+str(age)

a = kri("krishna", "reddy")

a.pprint(25)
a.pprint(40)