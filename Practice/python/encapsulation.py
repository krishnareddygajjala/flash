class Car:
 
    def __init__(self):
        pass
    def drive(self):
        print 'driving'
    def __updateSoftware(self):
        print 'updating software'
    def _update(self):
        print "updated"
 
redcar = Car()
redcar.drive()
redcar._update()
redcar._Car__updateSoftware() 
#redcar.__updateSoftware()  #not accesible from object.

class Car1:
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    def drive(self):
        print 'driving. maxspeed ' + str(self.__maxspeed)
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
 
edcar = Car1()
edcar.drive()
edcar.setMaxSpeed(320)
edcar.drive()
print edcar._Car1__maxspeed