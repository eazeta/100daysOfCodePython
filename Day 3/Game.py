print(f'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
******************************************************************************* \n
''')
print('Pirate: Welcome to Treasure Island!')
name = input('Pirate: What\'s your name captain? \nYou: ')
print(f'Pirate: Aaaah {name}! How could I forget! Let\'s begin!')

levelone = input('You wash up on an island. None of your crew in sight. You look to your left, nothing but a sandy beach. You look to your right and you see a forest. Which way do you go, left or right? \nEnter choice: ').capitalize()

if levelone == 'Left' or levelone == 'L':
  leveltwo = input('You keep walking and approach the edge of the island. You see another island with another a mansion on it. What do you do, swim or wait? \nEnter choice: ').capitalize()
  if leveltwo == 'Wait':
    print('You wait... \nand wait...\nThen you get bored of waiting and build a raft with some timber you find nearby.\nYou finally make it to the other island with the mansion and you see three doors, one blue, one red and one yellow.')
    levelthree = input('Which door do you walk through? Enter choice: ').capitalize()
    if levelthree == 'Blue' or levelthree == 'B':
      print('You get eaten by Beasts! Game over!')
    elif levelthree == 'Red' or levelthree == 'R':
      print('You get burned in a fire! Game over!')
    elif levelthree == 'Yellow' or levelthree == 'Y':
      print('You find gold! You Win!')
    else:
      print('You wonder around this new island looking for a different way in. You die of dehydration. Game over!')
  else:
    print('As you are swimming, you get attacked by a giant trout! Game over!')
    print(leveltwo)
else:
  print('You sprint into the forest and fall to your death in a hole! Game over!')