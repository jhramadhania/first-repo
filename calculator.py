print('==================')
print('Area Calculator 📐')
print('==================')
print('')

print('Choose your shape below!')
print('1. Triangle')
print('2. Rectangle')
print('3. Square')
print('4. Circle')
print('5. Quit')
print('')

shape = int(input('Which shape: '))

if shape == 1:
   print('')
   base = int(input('Base: '))
   height = int(input('Height: '))
   print('')
   print('The area is ' + str((base * height) / 2))
elif shape == 2:
   print('')
   length = int(input('Length: '))
   width = int(input('Width: '))
   print('')
   print('The area is ' + str(length * width))
elif shape == 3:
   print('')
   side = int(input('Side: '))
   print('')
   print('The area is ' + str(side ** 2))
elif shape == 4:
   print('')
   radius = int(input('Radius: '))
   print('')
   print('The area is ' + str(3.14 * (radius ** 2)))
elif shape == 5:
   print('Exit')
else:
   print('Input Error')