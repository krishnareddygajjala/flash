
class Sample_class(object):
    
    def __init__(self,name):
        self.name =  name
        
    def ur_name(self):
        print self.name
    
    def ur_age(self,age):
        print "your age is %s MR.%s"%(age,self.name)
        
    def ur_name_age(self,age):
        print "your age is %s MR.%s"%(age,self.name)
        
        
# a = Sample_class("krishna")
# b = Sample_class("sunil")
# a.ur_name()
# b.ur_name()
# a.ur_age(25)
# b.ur_age(22)
# Sample_class("reddy").ur_age(25)
