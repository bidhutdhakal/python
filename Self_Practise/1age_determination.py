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