"""
Reading a user presented file
"""

is_valid = False

while is_valid == False:
    try:
        filename = input("Enter desired filename: ")
        in_file = open(filename, "r")
        is_valid = True
    except FileNotFoundError:
        print("Error: File not found")

for line in in_file:
    line = line.strip()
    if line.startswith("#"):
        print(line)
in_file.close()