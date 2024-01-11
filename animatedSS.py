import turtle
import math
from planetclass import Planet
from solarsystem import SolarSystem
from sun import Sun

def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("Sun", 5000, 10, 5800)
    ss.addSun(sun)

    m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
    ss.addPlanet(m)

    m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
    moon = Planet("Moon", 1.2, 100, 0.01, 0, 2.0, "gray", orbitDistance=0.05, orbitSpeed=2)
    moon_distance = moon.getOrbitDistance()
    initial_moon_angle = 0 
    moon_x = m.getXPos() + moon_distance * math.cos(initial_moon_angle)
    moon_y = m.getYPos() + moon_distance * math.sin(initial_moon_angle)

    moon.moveTo(moon_x, moon_y)
    m.add_moon(moon)
    ss.addPlanet(m)

    m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
    ss.addPlanet(m)

    m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
    ss.addPlanet(m)


    ss.print_planets_by_distance()

    numTimePeriods = 200000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()