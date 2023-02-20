'''
Write a program that computes the surface area and the volume of a cone.
Radius and height are to be read from the console. [2 Points]

Hints:

  Surface area = pi * radius * slant height + pi * radius^2

  Slant height = sqrt(heigh^2 + radius^2)

  Volume = 1/3 * pi * radius^2 * height

  
  You can use the ** operator to compute the power (e.g., 2 ** 3 ==> 8)

Sample output:

  Please enter the radius: 4
  Please enter the height: 3
  The surface area is 113.09733552923255
  The volume is 50.26548245743669
'''

# pi is defined in the math module
from math import pi,sqrt

radius = input("Please enter the radius: ")
height = input("Please enter the height: ")

radius = int(radius)
height = int(height)

slant_height = sqrt(height**2 + radius**2)
surface_area = ( pi * radius * slant_height ) + ( pi * radius**2 ) 

volume = 1/3 * pi * radius**2 * height

print("The surface area is ",surface_area)
print("The volume is ",volume)

