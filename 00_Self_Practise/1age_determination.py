print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name = input("enter your name: ")
DoB = input("please enter your year of birth: ")
age = 2020 - int(DoB)
print()
print("*" * 50)
print("Hello " + name + ", your are " + "{0}".format(age) + " years old")
print("*" * 50)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
name = input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
print(age)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name = input("What is your good name? ")
year = int(2020)
dob = int(input("Hi {0},Please provide your Date of Birth: ".format(name)))
age = year - dob
print("You are {0} years old {1}.".format(age,name))

if 18 <= age < 31:
    print ("{0}, Welcome to the luxury holiday. This package is just for the people like you".format(name))

else:
    print("Sorry {0}, unfortunately our package is age restriction from 18-31".format(name))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import random
highest = 100
answer = random.randint(1, highest)
print (answer)

print ("Please guess the number between 1 to {}.".format(highest))
guess = int(input("Gussing number is: " ))


if guess == answer:
    print ("Congratz, you got it the very first time")

else:
    if guess > answer:
        print("Please guess a lower number")

    else:
        print("Please guess the higher number")

    guess = int(input("Gussing number is: " ))

    if guess > answer:
        print("Please guess a lower number")

    else:
        print("Please guess the higher number")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
