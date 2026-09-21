"""
Percentage completion task
"""

number_of_students_completed = int(input("How many students have done the test? "))
total_students = int(input("How many students are there in the class? "))
percentage = (number_of_students_completed/total_students) * 100
print(f"{percentage}% of students have done the test")