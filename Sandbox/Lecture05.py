"""
Lecture activities from module 5
"""
# Do this now:
def main():
    names = ["Fred", "Bob", "Daniel", "Ben"]
    ages = [12, 24, 107, 54]
    oldest_person = find_oldest_person(names, ages)
    print(f"The oldest person is {oldest_person}")

def find_oldest_person(names, ages):
    oldest_age = max(ages)
    oldest_age_index = ages.index(oldest_age)
    oldest_name = names[oldest_age_index]
    return oldest_name

name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
new_name = input("Name: ")
new_age = int(input("Age: "))
name_to_age[new_name] = new_age
# spacer = max(for name in len((list(name_to_age.keys())))
spacer = 0
for name in name_to_age.keys():
    if spacer < len(list(name_to_age.keys())):
        spacer = len(list(name_to_age.keys()))

for name, age in name_to_age.items():
    print(f"{name:{spacer}} - {age:3}")

main()