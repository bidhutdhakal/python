print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#age = input("please enter the age: ")
age = 24
print("Your age is " + str(age) + " years")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

age = 24
print("Your age is {0} years".format(age))
# NOTE: the replacement field is represented by {} followed by ".format()" at the end.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Note: when we want to replace, its denoted by .format() on first to last.
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# Note: ".format(), is initialized inside the print () value not outside.
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Note  We can use same format in any way as long as they are specified on the .format indexing format 0,1,2...sequence.
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




