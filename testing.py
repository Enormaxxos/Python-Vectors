from Vectors import Vector
from matrix import Matrix

kl = Vector(-1,-3,0)
km = Vector(-5,-5,-2)

a = Matrix("2 3 0;4 5 2")
print(a.table)

print(kl.cross(km).toString())