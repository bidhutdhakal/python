print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

available_exit = ["East", "West", "North", "South"]
chosen_exit = " "
while chosen_exit not in available_exit:
    chosen_exit = input("Please choose is direction: ")
# Note, here in above line, if input doesnot match the 'available exit' it keep itetrating until the input match list.

print("you just exited {}, Arent you clad you are out from there?".format(chosen_exit))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


