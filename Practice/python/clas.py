
class Car():
    def __init__(self,name,model,company,engine):
        self.name = name
        self.model = model
        self.company = company
        self.engine = engine
    def turn_engine(self):
        print "car name is %s" %(self.name)
        print "engine started "
    def brake(self):
        print "car stopped"
    def accelerate(self):
        print "car accelerate"
    def clutch(self):
        print "clutch"
    def blow_horn(self):
        print "horn"
    def add(self,a,b):
        return a+b

car = Car("ecosport","compact SUV","ford","1499cc")
car.turn_engine()
car.accelerate()
car.blow_horn()
car.clutch()
car.brake()