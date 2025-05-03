gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#----------------Question 1--------------------------
q1 = int(input('Q1. Do you like Dawn[1] or Dusk[2] ? '))

if q1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else: 
  print('Wrong input.')

#----------------Question 2---------------------------
q2 = int(input('Q2. When I am dead, I want people to remember me as: The Good[1], The Great[2], The Wise[3], The Bold[4] ? '))

if q2 == 1:
  hufflepuff = hufflepuff + 2
elif q2 == 2:
  slytherin = slytherin + 2
elif q2 == 3:
  ravenclaw = ravenclaw + 2
elif q2 == 4:
  gryffindor = gryffindor + 2
else:
  print('Wrong input.')

#----------------Question 3---------------------------
q3 = int(input('Q3. Which kind of instrument most pleases your ear: The violin[1], The trumpet[2], The piano[3], The drum[4] ? '))

if q3 == 1:
  slytherin = slytherin + 4
elif q3 == 2:
  hufflepuff = hufflepuff + 4
elif q3 == 3:
  ravenclaw = ravenclaw + 4
elif q3 == 4:
  gryffindor = gryffindor + 4
else:
  print('Wronginput.')

#print('Gryffindor : ', gryffindor)
#print('Ravenclaw : ', ravenclaw)
#print('Hufflepuff : ', hufflepuff)
#print('Slytherin : ', slytherin)

#-------------Sorting Hat Result----------------
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('Your house is 🦁 Gryffindor')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('Your house is 🦅 Ravenclaw')
elif hufflepuff >= slytherin:
  print('Your house is 🦡 Hufflepuff')
else:
  print('Your house is 🐍 Slytherin')