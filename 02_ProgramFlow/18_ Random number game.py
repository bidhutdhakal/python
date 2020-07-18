print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import random
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing.

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("you got it first time.")
else:
    if guess < answer:
        print ("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~While Unlimited~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import random
highest = 100
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing.
guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Congratz, you got it the first time.")
        break
    else:
        if guess < answer:
            print("Please guess higher: ")
        else:
            print("Please guess lower")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~While Unlimited with break~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import random
highest = 100
answer = random.randint(1, highest)
print(answer)
print("For exiting, type 0")

guess = 0

while guess != answer:
    guess = (int(input("Please enter the gussing number between 1 and {}: ".format(highest))))

    if guess == 0:
        print("Thank you for participating in guessing game.")
        break

    if guess == answer:
        print("Congratz, you guessed the correct number")
        break
    else:
        if guess > answer:
            print("Please guesss the lower number!")
        else:
            print("Please guess the higher number!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
