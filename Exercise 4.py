# ========= 4a =========
mark = int(input("4a) Enter mark (0-100): "))

# Outer if checks valid range
if 0 <= mark <= 100:
    # Inner if checks grade
    if mark > 74:
        print("Grade: Distinction")
    elif 60 <= mark <= 74:
        print("Grade: Merit")
    elif 40 <= mark <= 59:
        print("Grade: Pass")
    else:
        print("Grade: Fail")
else:
    print("Invalid mark. Must be between 0 and 100.")


# ========= 4b =========
x = input("4b) Enter first number: ")
y = input("Enter second number: ")

# Outer if checks if both are digits
if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    total = x + y
    print("Total:", total)
    if total > 100:
        print("Total is more than 100")
    else:
        print("Total is less than or equal to 100")
else:
    print("Both inputs must be numbers.")


# ========= 4c =========
print("4c) Menu")
print("1. Add")
print("2. Search")
print("3. Update")
print("4. Delete")

choice = int(input("Type 1–4: "))

# Outer if checks range
if 1 <= choice <= 4:
    # Inner if matches each action
    if choice == 1:
        print("Added")
    elif choice == 2:
        print("Searched")
    elif choice == 3:
        print("Updated")
    elif choice == 4:
        print("Deleted")
else:
    print("Invalid option. Must be between 1 and 4.")


# ========= 4d =========
import random

print("4d) Guessing game between 1 and 5.")
while True:
    num = random.randint(1, 5)
    guess = int(input("Guess the number (1–5): "))
    if guess == num:
        print("Correct! Generating new number...")
    else:
        print(f"Wrong! The number was {num}. Game over.")
        break


# ========= 4e =========
n = int(input("4e) Enter a number: "))

# Outer if checks range
if 0 <= n <= 100:
    # Inner if checks even or odd
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is out of range (0–100).")
