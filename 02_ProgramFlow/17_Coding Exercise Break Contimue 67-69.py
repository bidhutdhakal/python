print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Modify the code inside this loop to stop when i is exactly divisible by 11.
for i in range(0, 100, 7):
    print (i)
    if i > 0 and i % 11 == 0:
        break
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~With Continue~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Write a program to print out all the numbers from 0 to 10 that aren't divisible by 3 or 5.
for i in range(0,21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
# Note: in above statement if we use "and" in place of "or" then out put will be printed all number coz there is no
# Number that is divisible by 3 and 5 at the same time, except 15.
# Note: Remember> i % 5, here we are talking abt reminder. so it work.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~Without Continue~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Write a program to print out all the numbers from 0 to 10 that aren't divisible by 3 or 5.
for i in range(0,21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
# Note: here we use and statement coz we are using not equal to sign.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
