"""
Lecture activities from module 5
"""
# Do this now:
def main():
    names = ["Fred", "Bob", "Daniel", "Ben"]
    ages = [12, 24, 107, 20]
    oldest_person = find_oldest_person(names, ages)
    print(f"The oldest person is {oldest_person}")

def find_oldest_person(names, ages):
    oldest_age = max(ages)
    oldest_age_index = ages.index(oldest_age)
    oldest_name = names[oldest_age_index]
    return oldest_name

main()