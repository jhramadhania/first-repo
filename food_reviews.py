rating = float(input('Give us your review: '))

if rating > 4.5:
  print('Extraordinary')
elif rating <= 4.5 and rating > 4:
  print('Excellent')
elif rating <= 4 and rating > 3:
  print('Good')
elif rating <= 3 and rating > 2:
  print('Fair')
else:
  print('Poor')