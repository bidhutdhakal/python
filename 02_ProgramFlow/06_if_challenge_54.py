print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name = input("Please enter the name:    ")
age = int(input("please enter your age:     "))

# if age >= 18 and age <= 31: #or
if 18 <= age < 31 and name != "":  # and ensure that user enter the name or ignore it.
    print("Hello {0} , Welcome to the holiday vacation!!! ".format(name))
else:
    print("Sorry {0}, our ploicy only allow the person's aged from 18 - 30 for this vacation, and i am afraid yours is only {1}".format(name, age))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
