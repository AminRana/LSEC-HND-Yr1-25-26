# Kelly Scott - 70311205

import random

#4a)

def calculate_grade(mark : int) -> str:
    if mark > 74: return "distinction"
    if 60 <= mark <= 74: return "merit"
    if 40 <= mark <= 59: return "pass"
    return "fail"

student_name = input("Enter students name: ")
student_mark = int(input("Enter students grade: "))

if 0 < student_mark <= 100:
    print(f"{student_name} scored a {calculate_grade(student_mark)}!")

# 4b)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if isinstance(num1, int) and isinstance(num2, int):
    print(f"{num1} + {num2} = {num1 + num2}")

# 4c)

def get_menu_input() -> int:
    print("1. Add\n"
          "2. Search\n"
          "3. Update\n"
          "4. Delete")
    return int(input())

user_input = get_menu_input()

if 1 <= user_input <= 4:
    if user_input == 1:
        print("Added")
    elif user_input == 2:
        print("Searched")
    elif user_input == 3:
        print("Updated")
    elif user_input == 4:
        print("Deleted")

# 4d)

is_guess_correct = True

while is_guess_correct:
    random_num = random.randint(1, 5)
    guess = int(input("Enter guess (1 - 5): "))

    if not guess == random_num:
        print(f"Wrong! The number was {random_num}!")
        is_guess_correct = False
    else:
        print("Correct!")

# 4e)

num = int(input("Enter a number (1-100): "))

if 1 <= num <= 100:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Kelly Scott - 70311205