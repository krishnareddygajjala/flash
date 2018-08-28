from sample import Sample_class

class Sample_class_1(Sample_class):
    
    def __init__(self,name,last_name):
        # call parent constructor to set name
        
        super(Sample_class_1,self).__init__(name)
        #Sample_class.__init__(self, name)
        self.last_name = last_name
        
    print "sample class 1"
    def ur_name_age(self,age):
        print "your age is %s MR.%s %s"%(age,self.name,self.last_name)
 
   
a = Sample_class_1("krishna","reddy")
b = Sample_class("krishna")
a.ur_name()
a.ur_age(25)
a.ur_name()
a.ur_name_age(26)
a.ur_name_age(25) # method over riding
b.ur_name_age(25)