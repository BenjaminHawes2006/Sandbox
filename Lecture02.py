"""
Length Width Task
"""

length = int(input("Enter a length: "))
from random import randint
width = randint(0,length)
print(f"Width is {width}")
area = length * width
print(f"Area is {area}")


# Rows & Columns Task


def print_grid(number_of_rows, number_of_columns):
    for i in range(0,number_of_rows):
        print("*" * number_of_columns)
    print()

rows_count = int(input("Enter number of rows: "))
columns_count =  int(input("Enter number of columns: "))

print_grid(rows_count, columns_count)