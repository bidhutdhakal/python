print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~1(Slicing Backwards using a step in a Slice_32~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# index =                      2
# index =            1
# index =  012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]    # Because we are using negarive index, start value must be greater then ending value.
print(backwards)    # zyxwvutsrqponmlkjihgfedcb ==> up to but not including
print(letters[25::-1])  # zyxwvutsrqponmlkjihgfedcba ==> we are not determining the endvalue so it never stop & print a
print(letters[::-1])  # zyxwvutsrqponmlkjihgfedcba ==> end to start to print all.
print(letters[-4:])   # wxyz
print(letters[-1:])   # z
print(letters[:1])    # a
print(letters[0])     # a

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~2(Challenge~~~~~32~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Using the letters string from video, print output as follows

# index =                      2
# index =            1
# index =  012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"
# create a slice that produces the characters ==> # qpo.
print(letters[16:13:-1])
# Slice the string to produce ==> # edcba.
print(letters[4::-1])
# Slice the string to produce the last 8 characters, in reserve order. ==> # zyxwvuts
print(letters[25:17:-1])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DONE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

