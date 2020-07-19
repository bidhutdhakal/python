print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
for part in computer_parts:
    print(part)

print()
print(computer_parts[2])
print(computer_parts[0:3]) # Note: slicing will priduce another list, hence ans in [].
print(computer_parts[-1])


# Note: List will print the all the list including brackets.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts)

# Note: List will print the all the list including brackets.
# Note: if you print sequences, it will print with brackets.