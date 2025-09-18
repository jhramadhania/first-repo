from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    radius = 2440
elif random_planet == 'Venus':
    radius = 6052
elif random_planet == 'Earth':
    radius = 6371
elif random_planet == 'Mars':
    radius = 3390
elif random_planet == 'Saturn':
    radius = 58232
else:
    print("Oops! An error occured.")

print(f'The radius of {random_planet} is {radius} km')

area = 4 * pi * (radius ** 2)
print(f"The surface area of {random_planet} is {area} square kilometers")

rounded_area = round(area)     ##langsung dibulatkan
#rounded_area = round(area, 2) ##diambil 2 angka dibelakang koma
print(f'The rounded surface area of {random_planet} is {rounded_area} square kilometers')