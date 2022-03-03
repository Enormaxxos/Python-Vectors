from math import sqrt, atan2, pi, sin, cos, fabs, acos
from random import random


def degToRad(val):
    return val / 180 * pi


def radToDeg(val):
    return val / pi * 180


class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=None, y=None, z=None):
        if x is not None and isinstance(x, int):
            self.x = x
        if y is not None and isinstance(x, int):
            self.y = y
        if z is not None and isinstance(x, int):
            self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return True

    def sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.z = self.z - other.z
        return True

    def coefMult(self, coef):
        self.x = self.x * coef
        self.y = self.y * coef
        self.z = self.z * coef

        return True

    def dot(self, other):
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z

        return a + b + c

    def cross(self, other):
        a = self.y * other.z - self.z * other.y
        b = self.z * other.x - other.z * self.x
        c = self.x * other.y - self.y * other.x
        return Vector(a, b, c)

    def div(self, other):
        if other.x == 0 or other.y == 0 or other.z == 0:
            print("Vector.div() Error: Division by zero.")
            return False
        else:
            self.x = self.x / other.x
            self.y = self.y / other.y
            self.z = self.z / other.z
            return True

    def lerp(self, other, amt):
        self.x = self.x + (other.x - self.x) * amt
        self.y = self.y + (other.y - self.y) * amt
        self.z = self.z + (other.z - self.z) * amt

        return True

    def mag(self):
        a = sqrt(self.x ** 2 + self.y ** 2)
        return sqrt(a ** 2 + self.z ** 2)

    def normalize(self):
        coef = self.mag()
        if coef == 0:
            print("Vector.normalize() Error: Division by zero.")
            return False
        else:
            self.coefMult(1 / coef)
            return True


    def setMag(self, mag):
        self.normalize()
        self.coefMult(mag)
        return True

    def constrain(self,max):
        m = self.mag()
        if m > max:
            self.setMag(max)
        return True

    def heading(self, option=None):
        if self.z != 0:
            print("Vector.heading() Error: Method can only be used for 2D vectors.")
            return False
        else:
            final = atan2(self.y, self.x)
            if option == "rad" or option is None:
                return final
            elif option == "deg":
                return radToDeg(final)

    def setHeading(self, angle):
        m = self.mag()
        self.x = cos(angle)
        self.y = sin(angle)
        self.setMag(m)

        return True

    def setHeadingDeg(self, angle):
        m = self.mag()
        angle = degToRad(angle)
        self.x = cos(angle)
        self.y = sin(angle)

        return True

    def rotate(self, angle):
        newAngle = self.heading("rad") + angle
        self.setHeading(newAngle)

        return True

    def rotateDeg(self,angle):
        newAngle = self.heading("deg") + angle
        self.setHeadingDeg(newAngle)

        return True

    def angleBetween(self, other, option=None):
        a = self.dot(other)
        b = self.mag() * other.mag()

        if option is None or option == "rad":
            return acos(a / b)
        elif option == "deg":
            return radToDeg(acos(a / b))

    def dist(self, other):
        return sqrt(fabs(self.x - other.x) ** 2 + fabs(self.y - other.y) ** 2 + fabs(self.z - other.z) ** 2)

    def random2D(self):
        minusX = random()
        minusY = random()

        x = random()
        y = random()

        if minusX > 0.5:
            x = -x
        if minusY > 0.5:
            y = -y

        return Vector(x, y)

    def random3D(self):
        minusX = random()
        minusY = random()
        minusZ = random()

        x = random()
        y = random()
        z = random()

        if minusX > 0.5:
            x = -x
        if minusY > 0.5:
            y = -y
        if minusZ > 0.5:
            z = -z

        return Vector(x, y, z)

    def fromAngle(self, angle, length):
        try:
            a = Vector(cos(angle), sin(angle))
            a.setMag(length)
            return a
        except:
            print("something went wrong")
            return False

    def toString(self):
        return f"x:{self.x}, y:{self.y}, z:{self.z}"