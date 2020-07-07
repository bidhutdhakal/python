print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Note: up to but not including the ending value. in range it will always start with the indicated value.
for i in range(1, 20):
    print("i is now {0}".format(i))
# Output will be 1 to 19.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(1, 21):
    print("i is now {0}".format(i))
# Output will be 1 to 20.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~(For loop Challenge~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(0, 10):
    print("The number printing now is {0}".format(i))
# printing number 0-9
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(0, 10, 2):
    print("The number printing now is {0}".format(i))

# Note: printing number 0 to 10 in the difference of 2 interval starting from zero

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(10, 0, -2):
    print("The number printing now is {0}".format(i))
# Note: printing number from 10 to 0 in the interval of -2
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

# Note; if range will run one time, but for will run for multiple time. observe 6 and 7

age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
for age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

