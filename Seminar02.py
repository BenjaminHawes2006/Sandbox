"""
Seminar 2 Tasks
"""

# number_of_students_completed = int(input("How many students have done the test? "))
# number_of_total_students = int(input("How many students are there in the class? "))
# percentage = (number_of_students_completed/number_of_total_students) * 100
# print(f"{percentage}% of students have done the test")

lower_limit = int(input("Enter a lower limit: "))
upper_limit = int(input("Enter an upper limit: "))

if upper_limit <= lower_limit:
    print("Invalid limits")
    lower_limit = int(input("Enter a lower limit: "))
    upper_limit = int(input("Enter an upper limit: "))
else:
    from random import randint

    smiley_face_count = randint(lower_limit, upper_limit)
    print(":D " * smiley_face_count)
