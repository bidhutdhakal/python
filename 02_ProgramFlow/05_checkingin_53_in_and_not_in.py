print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1_in~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
parrot = "Norwegian Blue"
letter = input("Enter a Character: ")

if letter in parrot:
    print("{0} is in {1}".format(letter, parrot))
else:
    print("I don't need that letter")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2_not_in~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

activity = input("What would you like to do today?")

if "cinema" not in activity:
    print("But i want to go to cinema")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3_not_in~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

activity = input("What would you like to do today?")
# Note: Casefold converts the strings into the lower cases
if "cinema" not in activity.casefold():
    print("But i want to go to cinema")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4_not_in~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
