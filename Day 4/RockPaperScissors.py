import random as r
end = 'N'
print("Welcome to Rock Paper Scissors!")
while end != 'Y':
  play = int(input('Enter 0 for Rock, 1 for Paper or 2 for Scissors: '))
  computer = r.randint(0, 2)
  if play == computer:
      print("Draw!")
  elif play == 0 and computer == 2 or play == 1 and computer == 0 or play == 2 and computer == 1:
      print("You win!")
  else:
      print("You lose!")
  end = input('Would you like to close the game? Type Y to close or type N to play another round. Enter: ').capitalize()
