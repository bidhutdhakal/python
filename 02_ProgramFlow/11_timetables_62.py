print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range (1, 6):
    for j in range (1, 11):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("_________________________")
# Note: Last print is indented below the for j loop so it will print after complete of its iteration.
# Note: if its on line below print then it will print in every line, while if its print on the initial of i for, it will print onlny one time.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
