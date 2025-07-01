import random

question = input('Question: ')
num = random.randint(1, 9)

if num == 1:
  response = 'Yes - definitely.'
elif num == 2:
  response = 'It is decidedly so.'
elif num == 3:
  response = 'Without a doubt.'
elif num == 4:
  response = 'Reply hazy, try again.'
elif num == 5:
 response = 'Ask again later.'
elif num == 6:
  response = 'Better not tell you now.'
elif num == 7:
  response = 'My sources say no.'
elif num == 8:
  response = 'Outlook not so good.'
else:
  response = 'Very doubtful.'

print('Magic 8 ball: ', response)