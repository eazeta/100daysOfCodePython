#Ceasar Cyper shifts the alphabet by a certain amount

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Function to encrypt message
def encode(message, shift):

  encryptedMessage = []

  listMessage = list(message)
  for letter in listMessage:
    position = alphabet.index(letter)
    newposition = position + shift
    if newposition > 25:
      multiplier = newposition//26 #Double backslash is floor division
      newposition -= (26 * multiplier)
    encryptedMessage.append(alphabet[newposition])
  
  print(''.join(encryptedMessage))

#Function to decrypt message
def decode(message, shift):

  decryptedMessage = []

  listMessage = list(message)
  for letter in listMessage:
    position = alphabet.index(letter)
    newposition = position - shift
    if newposition < 1:
      multiplier = newposition//26 #Double backslash is floor division
      newposition += abs(26 * multiplier)
    decryptedMessage.append(alphabet[newposition])
  
  print(''.join(decryptedMessage))

  

message = input("Enter your message: \n").lower()
shift = int(input("Enter your shift: \n"))

toDo = input("Enter 'e' for Encryption and 'd' for Decryption: ").lower()

if toDo == 'e':
  encode(message, shift)
elif toDo == 'd':
  decode(message, shift)
else:
  print("error")