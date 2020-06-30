print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# If statement with blocks.
name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))
print(age)

# we can do multiple line comment or uncomment by "control + /"

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

# Doing same as above but in opposite way. Please observe the diff.
# for debugging, make sure you click left and get red dot on your line to check the parameter.
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")

else:
    print("You are old enough to vote")
    print("Please put an X in the box")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

