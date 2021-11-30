from Vectors import Vector,degToRad,radToDeg
from random import random,randrange
from math import sqrt

class Ball:
    pos = Vector()
    vel = Vector().random2D()

    def __init__(self, maxVel):
        self.pos.x = randrange(800)
        self.pos.y = randrange(800)

        self.vel.setMag(sqrt((maxVel**2/2)))

    def update(self):
        self.pos.add(self.vel)

        if self.pos.x < 0 or self.pos.x > 800:
            self.vel.x = -self.vel.x
        if self.pos.y < 0 or self.pos.y > 800:
            self.vel.y = -self.vel.y