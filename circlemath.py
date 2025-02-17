import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)
diameter = radius * 2
print(f"the area of the circle is {round(area,2)} cm², its diameter is {diameter}")
