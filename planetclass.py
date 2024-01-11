import turtle
import math
class Planet:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC, orbitDistance=0, orbitSpeed=0):
        self.__current_angle = 0
        self.__moons = []

        self.__orbitDistance = orbitDistance
        self.__orbitSpeed = orbitSpeed
        
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy 

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        size_scale = iRad / 100 
        self.__pTurtle.shapesize(stretch_wid=size_scale, stretch_len=size_scale)


        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance

    def getVolume(self):
        import math
        v = 4/3 * math.pi * self.__radius**3
        return v

    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius**2
        return sa

    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def setName(self, newName):
        self.__name = newName 

    def setRadius(self, newRadius):
        self.__radius = newRadius 

    def setMass(self, newMass):
        self.__mass = newMass 

    def setDistance(self, newDistance):
        self.__distance = newDistance 

    def __str__(self):
        return self.__name
      
    def __lt__(self, otherPlanet):
        return self.__distance < otherPlanet.__distance

    def __gt__(self, otherPlanet):
        return self.__distance > otherPlanet.__distance  


    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy


    def add_moon(self, moon):
        self.__moons.append(moon)

    def get_moons(self):
        return self.__moons
    
    def update_angle(self, angle_increment):
        self.__current_angle += angle_increment
        return self.__current_angle

    def getOrbitSpeed(self):
        return self.__orbitSpeed
    
    def getOrbitDistance(self):
        return self.__orbitDistance
    
    def get_current_angle(self):
        return self.__current_angle