import random

ileRund=int(input('Ile rund chcesz grac?: '))
lista=['Paper', 'Rock', 'Scissors']
a=['Paper', 'paper']
b=['Rock', 'rock']
c=['Scissors', 'scissors']

userCounts=0
computerCounts=0

for x in range(ileRund):
    user=input('Podaj wartość: Paper/paper, Rock/rock, Scissors/scissors: ')
    while user not in ['Paper','paper', 'Rock', 'rock', 'Scissors', 'scissors']:
      user=input('Podałeś błędną wartość. Podaj wartość z wybranych: Paper/paper, Rock/rock, Scissors/scissors: ')
    computer=random.choice(lista)
    print(computer)
    if (user in a and computer=='Paper'):
      print('Remis!')
    elif (user in a and computer=='Rock'):
      print('Twoja wygrana!')
      userCounts+=1
    elif (user in a and computer=='Scissors'):
      print('Wygrana po stronie komputera!')
      computerCounts+=1
    elif (user in b and computer=='Paper'):
      print('Wygrana po stronie komputera!')
      computerCounts+=1
    elif (user in b and computer=='Rock'):
      print('Remis!')
    elif (user in b and computer=='Scissors'):
      print('Twoja wygrana!')
      userCounts+=1
    elif (user in c and computer=='Paper'):
      print('Twoja wygrana!')
      userCounts+=1 
    elif (user in c and computer=='Rock'):
      print('Wygrana po stronie komputera!')
      computerCounts+=1
    elif (user in c and computer=='Scissors'):
      print('Remis!')  
if userCounts>computerCounts:
  if userCounts-computerCounts==1:
    print('Wygrywasz grę 1 punktem!')
  elif userCounts-computerCounts>1:
    print('Wygrywasz grę %.0f punktami!' % userCounts)
elif userCounts<computerCounts:
  if computerCounts-userCounts==1:
    print('Przegrałeś grę 1 punktem.')
  elif computerCounts-userCounts>1:
    print('Przegrałeś grę %.0f punktami.' % (computerCounts-userCounts))

