print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "spam"
found_at = None

# for index in range(6):
# Note: len in line 9 stands for length while we use index to find the exact indexing spot.
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
# Note: adding break in line 11 coz we dont want out program to run again and again. after the search is complete.
print("The item found at position {0}".format(found_at))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "albatross"
# Note: found_at = None is really important at line 4 becasue if item is not in the list then it should let us know.
# meaning it will never enter the loop when its not found and directly execute print.
found_at = None

# for index in range(6):
# Note: len in line 9 stands for length while we use index to find the exact indexing spot.
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
# Note: adding break in line 11 coz we dont want out program to run again and again. after the search is complete.
print("The item found at position {0}".format(found_at))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "albatross"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("The item found at position {0}".format(found_at))
else:
    print("{}, not found".format(item_to_find))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "albatross"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("The item found at position {0}".format(found_at))
else:
    print("{}, not found".format(item_to_find))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "pasta"
found_at = None

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("The item found at position {0}".format(found_at))
else:
    print("{}, not found".format(item_to_find))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
