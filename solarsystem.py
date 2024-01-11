import turtle
import math
class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)
            
    def movePlanets(self):
        G = .1
        dt = .001

        # First update all planets' positions
        for p in self.__planets:
            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX/r**3
            accY = G * self.__theSun.getMass() * rY/r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)
            
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

        # Then update all moons' positions relative to their planet
        for p in self.__planets:
            for moon in p.get_moons():
                moon_angle = moon.get_current_angle() + dt * moon.getOrbitSpeed()
                moon.update_angle(moon_angle)
                moon_x = p.getXPos() + moon.getOrbitDistance() * math.cos(moon_angle)
                moon_y = p.getYPos() + moon.getOrbitDistance() * math.sin(moon_angle)

                moon.moveTo(moon_x, moon_y)

    def freeze(self):
        self.__ssScreen.exitonclick()
    
    def print_planets_by_distance(self):
        sorted_planets = sorted(self.__planets, key=lambda planet: planet.getDistance(), reverse=True)
        for planet in sorted_planets:
            print(planet.getName())
        print(self.__theSun.getName())
