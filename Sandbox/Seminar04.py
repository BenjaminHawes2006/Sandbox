"""
Activities from week 4 seminar
"""
# Do-this-now
names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do we want to remove? ")
while name_to_remove != "":
    if name_to_remove not in names:
        print("Name not found!")
        name_to_remove = input("Who do we want to remove? ")
    else:
        names.remove(name_to_remove)
        print(", ".join(names))
        name_to_remove = input("Who do we want to remove? ")
print("Closing the program...")

# Variable names
# 1) numbers
# 2) number_of_people
# 3) person_age
# 4) 2D_data_points
# 5) is_mutant
# 6) list_index

# Dynamic output
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
for pair in data:
    print(f"{pair[0]:11} = {pair[1]:3}")
