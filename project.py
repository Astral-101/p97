import random

number = random.randint(1, 10)
myNumber = None

while myNumber != number:
    myNumber = input("Guess a number between 1 and 10")
    myNumber = int(myNumber)

    if (myNumber == number):
        print("You got the number!")
        break

    elif(myNumber > number):
        print("Try a number a little bit lower")

    else:
        print("Try a number a little higher")