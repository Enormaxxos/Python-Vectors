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
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    def add(self, other):
        try:
            self.x += other.x
            self.y += other.y
            self.z += other.z
        except:
            print("Something went wrong")
            return False
        return True

    def sub(self, other):
        try:
            self.x = self.x - other.x
            self.y = self.y - other.y
            self.z = self.z - other.z
        except:
            print("Something went wrong")
            return False
        return True

    def coefMult(self, coef):
        try:
            self.x = self.x * coef
            self.y = self.y * coef
            self.z = self.z * coef
        except:
            print("Something went wrong")
            return False
        return True

    def dot(self, other):
        try:
            a = self.x * other.x
            b = self.y * other.y
            c = self.z * other.z

            return a + b + c
        except:
            print("something went wrong")
            return False

    def cross(self, other):
        if self.z == 0 or other.z == 0:
            print("Error: Only works for two 3D Vectors.")
            return False
        else:
            a = self.y * other.z - self.z * other.y
            b = self.z * other.x - other.z * self.x
            c = self.x * other.y - self.y * other.x
            return Vector(a, b, c)

    def div(self, other):
        try:
            self.x = self.x / other.x
            self.y = self.y / other.y
            if other.z != 0:
                self.z = self.z / other.z
            else:
                print("Error: Division by zero.")
        except:
            print("Something went wrong")
            return False
        return True

    def mag(self):
        a = sqrt(self.x ** 2 + self.y ** 2)
        return sqrt(a ** 2 + self.z ** 2)

    def normalize(self):
        try:
            coef = self.mag()
            self.coefMult(1 / coef)
        except:
            print("something went wrong")
            return False
        return True

    def setMag(self, mag):
        try:
            self.normalize()
            self.coefMult(mag)
        except:
            print("something went wrong")
            return False
        return True

    def heading(self, option=None):
        if self.z != 0:
            print("Error: Method Vector.heading() can only be used for 2D vectors.")
            return False
        else:
            try:
                final = atan2(self.y, self.x)
                if option == "rad" or option is None:
                    return final
                elif option == "deg":
                    return radToDeg(final)
            except:
                print("something went wrong")
                return False

    def setHeading(self, angle):
        try:
            m = self.mag()
            self.x = cos(angle)
            self.y = sin(angle)
            self.setMag(m)
        except:
            print("something went wrong")
            return False
        return True

    def rotate(self, angle):
        try:
            newAngle = self.heading("rad") + angle
            self.setHeading(newAngle)
        except:
            print("something went wrong")
            return False
        return True

    def angleBetween(self, other, option=None):
        a = self.dot(other)
        b = self.mag() * other.mag()

        if option is None or option == "rad":
            return acos(a / b)
        elif option == "deg":
            return radToDeg(acos(a / b))

    def dist(self, other):
        try:
            a = sqrt(fabs(self.x - other.x) ** 2 + fabs(self.y - other.y) ** 2)
            return sqrt(a ** 2 + fabs(self.z - other.z) ** 2)
        except:
            print("something went wrong")
            return False

    def lerp(self, other, amount):
        try:
            self.x = self.x + (other.x - self.x) * amount
            self.y = self.y + (other.y - self.y) * amount
            self.z = self.z + (other.z - self.z) * amount
        except:
            print("something went wrong")
            return False
        return True

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
