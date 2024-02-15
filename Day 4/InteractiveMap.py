line1 = ["O","O","O"]
line2 = ["O","O","O"]
line3 = ["O","O","O"]
map = [line1,line2,line3]

hideTreasure = input("Where would you like to hide the treasure on the map? ")

firstCoOrd = hideTreasure[0]
secondCoOrd = hideTreasure[1]

map[int(firstCoOrd)][int(secondCoOrd)] = "X"

print(line1)
print(line2)
print(line3)