print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])    #==> programmind number start at 0,1,2,3

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#                    1
#         01234567890123
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(parrot)
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(parrot)
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#                    1
#          01234567890123
#parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg (upto but not including)
print(parrot[5:5])  # we (Remember upto but not including)
print(parrot[0:9])  # Norwegin (Remember upto but not includinf)
print(parrot[:9])  # Norwegin (Same value)
print(parrot[10:14])    # Print the value Blue
print(parrot[10:])      # Print the value Blue without giving the end index value
print(parrot[:6])   # Norweg
print(parrot[6:])   # ian Blue
print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:])    # since there is no start and stop, it will print all.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~5(Slicing with Negative Number~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#                    1
#          01234567890123
#parrot = "Norwegian Blue"

print(parrot[-4:-2])        # Bl ==> make sure number is in --> format.
print(parrot[-4:12])        # Bl
print(parrot[0:6])          # Norweg
print(parrot[-14:-8])             # Norweg ==> remember up to but not including.


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~6(Slicing using a step in a Slice~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#                    1
#          01234567890123
#parrot = "Norwegian Blue"

print(parrot[0:6:2])        # Nre   ==> 0 to 6 but not including and then skipping on ratio of 2
print(parrot[0:6:3])        # Nw    ==> 0 to 6 but not including and then skipping on ratio of 3

number = "9,223,372,036,854,775,807"

print(number[0::4])     # 9326457  ==> Start to the ratio of 4, then start where the ratio stops to the next 4 including
print(number[1::4])     # 9326457  ==> Start to the ratio of 4, then start where the ratio stops to the next 4 including

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")









