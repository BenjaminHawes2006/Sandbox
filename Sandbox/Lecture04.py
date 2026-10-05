"""
Python file containing activities from module four lecture videos
"""

# Do-this-now (1)

names = ["Ben", "Joel", "Daniel", "Hayden", "Lauren"]
is_finished = False

while not is_finished:
    try:
        names_index = int(input("Enter the desired index for the list: "))
        if names_index > 0:
            print(f"That name is {names[names_index - 1]}")
        elif names_index < 0:
            print(f"That name is {names[names_index]}")
        else:
            print(names["Zero"])
        is_finished = True
    except IndexError:
        print("Improper index! Try again")
    except TypeError:
        print("Improper index! Try again")