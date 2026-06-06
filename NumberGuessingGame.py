import random

mine = random.randint(1, 10)

guess = int(input("Guess a number between 1 to 10 "))

if guess == mine:
    print("You have it right \n You win \n Congratulations!")
    print("The number was: ", mine)
elif guess > mine:
    print("Close, dear, but it is bigger than your number")
    print("The number was: ", mine)
elif guess < mine:
    print("Close, dear, but it is smaller than your number")
    print("The number was: ", mine)
else:
    print("Sorry dear")