"""
Activities from week 4 seminar
"""

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

