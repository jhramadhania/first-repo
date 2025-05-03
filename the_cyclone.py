height = int(input('Your height: '))
credit = int(input('Your credit: '))

if height >= 137 and credit >= 10:
  response = 'Enjoy the ride!'
elif height < 137 and credit >= 10:
  response = 'You are not tall enough to ride.'
elif height >= 137 and credit < 10:
  response = 'You do not have enough credits.'
else:
  response = 'You have not met either requirement.'

print('Result: ', response)