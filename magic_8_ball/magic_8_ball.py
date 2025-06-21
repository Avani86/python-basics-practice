# Magic 8 Ball

import random

Question = input('Question:  ')

random = random.randint(1, 9)

if random == 1:
 answer = 'Yes - definitely'
elif random == 2:
  answer = 'It is decidedly so'
elif random == 3:
   answer = 'Without a doubt'
elif random == 4:
  answer = 'Reply hazy, try again'
elif random == 5:
  answer = 'Ask again later'
elif random == 6:
  answer = 'Better not tell you now'
elif random == 7:
  anwer = 'My sourcfes say no'
elif random == 8:
  anwer = 'Outlook not so good'
elif random == 9:
  answer = 'Very doubtful'
else:
  anwer = 'Error'

print('Magic ball 8  '  +   answer)






    







