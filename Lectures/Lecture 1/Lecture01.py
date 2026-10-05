"""
first demo
"""
name = input("Name: ")
print("Hello", name)

cost = float(input("Enter monthly cost: $"))
yearCost = 12 * cost

print(f"Yearly cost is ${yearCost:.2f}")

age = float(input("Enter your age: "))
if age <= 4:
    print("You are a baby")
elif age <= 17:
    print("You are a child")
elif age <= 65:
    print("You are an adult")
else:
    print("You are old")