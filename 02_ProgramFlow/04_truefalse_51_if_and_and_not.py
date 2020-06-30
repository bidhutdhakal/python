print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
day = "Monday"
temperature = 30
raining = True
# Note: raining is T and on if condition its and not which makes the cond false so its learn python/
if day == "Saturday" and temperature > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Python")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
day = "Saturday"
temperature = 30
raining = True
# Note: here the condition is or not so we get the condition true for all and we get Go Swimming.
if day == "Saturday" and temperature > 27 or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
day = "Saturday"
temperature = 28
raining = True
# Note: here the condition is or not so we get the condition true for all and we get Go Swimming.
# Note: always use (perenthesis () ) when using "and" and "or"
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
