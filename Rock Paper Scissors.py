t = ['rock', 'paper', 'scissors'] 
print('')
print("Rock Paper Scissors, a project by Max and Lucas. Get to 5 and you win!\n\n")
from random import shuffle
playerscore = 0
computerscore = 0
s = 1
while s == 1:  
  shuffle(t)
  computer = t[0]
  print("")
  player = input('Do you choose Rock, Paper or Scissors?\n')
  if computer == player.strip(' ').lower():
    print ('It\'s a Tie!')
    playerscore += 1
    computerscore += 1
  elif computer == 'rock' and player.strip(' ').lower() == 'paper':
    print("")
    print ('Paper covers Rock! You win!')
    playerscore += 1
  elif computer == 'rock' and player.strip(' ').lower() == 'scissors':
    print("")
    print ("Rock crushes Scissors. Sorry, you lose.")
    computerscore += 1
  elif computer == 'scissors' and player.strip(' ').lower()== 'rock':
    print("")
    print('Rock crushes Scissors. You win!')
    playerscore += 1
  elif computer == 'scissors' and player.strip(' ').lower() == 'paper':
    print("")
    print('Scissor cut Paper. You lose!')
    computerscore += 1
  elif computer == 'paper' and player.strip(' ').lower()== 'rock':
    print("")
    print('Paper covers Rock! Sorry, you lose.')
    computerscore += 1
  elif computer == 'paper' and player.strip(' ').lower()== 'scissors':
    print("")
    print('Paper is sliced by Scissors. You win!')
    playerscore += 1
  else:
    print("")
    print('That is not an option.')
  if computerscore > playerscore:
    print('You are losing ' + str(computerscore) + ' to ' + str(playerscore) + '.')
  elif playerscore > computerscore:
    print('You are winning ' + str(playerscore) + ' to ' + str(computerscore) + '.')
  elif playerscore == computerscore:
    print('You are tied, '+str(playerscore)+' to '+str(computerscore)+'.')
  if playerscore == 5 and computerscore < 5:
    print('')
    print ('You win, 5 to ' + str(computerscore) + '! Restart this program to play again.')
    quit()
  elif playerscore == 5 and computerscore == 5:
    print("")
    print ('It\'s a tie! Restart the program to play again.')
    quit()
  elif playerscore < 5 and computerscore == 5:
    print("")
    print('The computer wins, 5 to ' + str(playerscore) + '! Better luck next time.')
    quit()
  else:
    input('Press enter to keep playing.')
