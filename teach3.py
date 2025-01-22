square = float(input('Input a length value in centimeters: '))
area = square ** 2
import math 
circle = (square ** 2) * math.pi
cube = (square ** 3)
sphere = (4/3) * (square ** 3) * math.pi

square_meters = area / 100
circle_meters = circle / 100
cube_meters = cube / 100
sphere_meters = sphere / 100

print(f"If this were the length of a square, that square's area would be {area} in square centimeters.")
print(f"The area in square meters would be {square_meters}.")
print(f"If this were the radius of a circle, that circle's area would be {circle} in square centimeters.")
print(f"The area in square meters would be {circle_meters}.")
print(f"If this were the length of a cube, that cube's volume would be {cube} in cubic centimeters.")
print(f"The volume in cubic meters would be {cube_meters}.")
print(f"If this were the radius of a sphere, that sphere's volume would be {sphere} cubic centimeters.")
print(f"The volume in cubic meters would be {sphere_meters}.")

length = float(input('What is the length of the rectangle in centimeters? '))
width = float(input('What is the width of the rectangle in centimeters? '))
rectangle = length * width
rectangle_meters = rectangle / 100
print(f'The are of the rectangle is {rectangle} square centimeters.')
print(f'The area in meters would be {rectangle_meters} square meters.')