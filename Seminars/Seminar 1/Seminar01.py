"""
GST Task
"""
item_price = float(input("Enter Unit Price: $"))
GST_response = input("Is there GST? (y/n) ")
final_price = item_price
GST_Rate = 0.1
if GST_response == "y":
     final_price =  (GST_Rate * item_price) + item_price

print(f"Your final price is ${final_price:.2f}")

"""
Loops Task
"""

count = 1

for count in range(1,101):
    print(count)
else:
    print("For loop count completed")

count = 1

while count < 100:
    print(count)
    count += 1

print("While loop count completed")

"""
Secret Number Task
"""

secret_number = 3

while float(input("Enter your guess: ")) != secret_number:
    print("Wrong! Idiot!")

else:
    print(f"Correct! The secret number was {secret_number}")
