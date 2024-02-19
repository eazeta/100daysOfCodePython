## A prime number is a number which is only divisible by itself or by 1

def isPrime(number):
  isPrimeNumber = False

  if number == 1 or number == 2:
    print("This is a prime number")
  elif number == 0:
    print("bruh")
  else:
    for i in range(2,number):
      check = number % i
      if check == 0:
        isPrimeNumber = False
        break
      else:
        isPrimeNumber = True

    if isPrimeNumber == True:
      print("This is a prime number")
    else:
      print("This is not a prime number")

numberInput = int(input("Enter a number: "))
isPrime(numberInput)