print("Welcome to the Tip Calculator!")
total = int(input("What was the total bill? £"))
split = int(input("How many people would like to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10%, 12% or 15%? "))

payment = (total + ((total * percentage)/100)) / split

print("Each person should pay £" + str(payment))
