print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list as 32 is divisible by 8 and its remainder is zero.
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
