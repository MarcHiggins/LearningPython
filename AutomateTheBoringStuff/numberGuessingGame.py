import random

secretNumber = random.randint(1, 2001)
print(secretNumber)

print("I am thinking of a number between 1 and 2000")
print("You have six guesses!")

for guessesTaken in range(1,7):
    print ("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low!")
    elif guess > secretNumber:
        print("Your guess is too high!")
    else:
        break
    
if guess == secretNumber:
    print("Well done, you guessed the secret number in " + str(guessesTaken) + " guesses")
else:
    print ("Nope the number was " + str(secretNumber))

