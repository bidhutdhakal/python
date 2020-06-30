print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = 5

print("Please guess the number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed incorrectly")
#
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed incorrectly")
#
# else:
#     print("You are correct!!!")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Using if with string, write a small program that assigns name of 2 trees to 2 variables, called tree1 and tree2/
# of the values of the variables are equal, print the massage "The trees are the same" otherwise print "the trees are
# different".
tree1 = 'pine'
tree2 = 'pine'

# add the code to compare the trees
if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4( Same using not equal)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:       # guess must be greater than answer.
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it right")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5( Same using equal)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = 5
guess = int(input("Please Guess the Number: "))

if guess == answer:
    print("Well Done, you got it the very first time")

else:
    if guess > answer:
        print("Please Guess lower then this")
        guess = int(input("Please enter the number"))
        if guess == answer:
            print("Well Done, you got it the first time")
        else:
            print("Sorry you didnt get it correct.")

    elif guess < answer:
        print("Please Guess higher then this")
        guess = int(input("Please enter the number"))
        if guess == answer:
            print("Well Done, you got it the first time")
        else:
            print("Sorry you didnt get it correct.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
