import random
rps = int(input(' Type: 1 for Rock, 2 for Paper, 3 for Scissors'))

comp = random.randint(1,3)

if rps == 1:
  print('You: ✊')
elif rps == 2:
  print('You: ✋')
elif rps == 3:
  print('You: ✌️')

if comp == 1:
  print('Computer: ✊')
elif comp == 2:
  print('Computer: ✋')
elif comp == 3:
  print('Computer: ✌️')

if rps == 1 and comp ==2:
  win = 1
elif rps == 1 and comp ==3:
  win = 0
elif rps == 1 and comp == 1:
  win = 2
elif rps == 2 and comp ==2:
  win = 2
elif rps == 2 and comp ==3:
  win = 1
elif rps == 2 and comp == 1:
  win = 0
elif rps == 3 and comp ==2:
  win = 0
elif rps == 3 and comp ==3:
  win = 2
elif rps == 3 and comp == 1:
  win = 1

if win == 0:
  print('You won')
elif win ==1:
  print('Computer won')
elif win == 2:
  print('Draw')


