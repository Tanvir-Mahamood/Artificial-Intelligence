import math
print(math.pi)
print(math.e)
print(math.sqrt(3))
print(math.floor(-3.14))

r = float(input("Enter radius "))
area = math.pi * r * r
print(f"Area of circle = {area}")
print(f"Area of circle = {round(area, 2)}")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"sqrt({a}^2 + {b}^2) = {c}")

print(a == int(a))
