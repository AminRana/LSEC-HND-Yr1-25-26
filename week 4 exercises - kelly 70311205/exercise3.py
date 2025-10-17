# Kelly Scott - 70311205

# 3a)
def calculate_grade(mark : int) -> str:
    if mark > 74: return "distinction"
    if 60 <= mark <= 74: return "merit"
    if 40 <= mark <= 59: return "pass"
    return "fail"

student_name = input("Enter students name: ")
student_mark = int(input("Enter students grade: "))

print(f"{student_name} scored a {calculate_grade(student_mark)}!")

# 3b)

def get_word_length(word : str) -> str:
    word_length = len(word)
    if 1 <= word_length <= 3: return "too short word"
    if 4 <= word_length <= 8: return "small word"
    if 9 <= word_length <= 12: return "big word"
    return "too big word"

user_input = input("Enter a word: ")

print(f"That is a {get_word_length(user_input)}!")

# 3c)
def get_menu_input() -> int:
    print("1. Add\n"
          "2. Search\n"
          "3. Update\n"
          "4. Delete")
    return int(input())

user_input = get_menu_input()

if user_input == 1:
    print("Added")
elif user_input == 2:
    print("Searched")
elif user_input == 3:
    print("Updated")
elif user_input == 4:
    print("Deleted")
else:
    print("Wrong command")

# 3d)

professions = {"teacher": 25,
               "doctor": 60,
               "lawyer": 200,
               "driver": 15}

user_input = input("What profession?\n")

if professions.__contains__(user_input):
    print(f"You make £{professions[user_input]}/h!")
else:
    print("Profession not found :(")

#3e)

def calculate_tax(gross_salary : float) -> float:
    tax = 0.0
    if gross_salary <= 12570:
        return tax
    else:
        if 12570 < gross_salary <= 50270:
            tax += (gross_salary - 12750) * 0.2
        elif 50270 < gross_salary <= 125140:
            tax += (gross_salary - 50270) * 0.4
        elif gross_salary > 125140:
            tax += (gross_salary - 125140) * 0.45
    return tax

def calculate_net_salary(gross_salary : float, tax : float) -> float:
    return gross_salary - tax

gross_salary = float(input("Enter gross salary: "))
tax = calculate_tax(gross_salary)
print(f"You pay £{tax : .2f} in taxes, with a net salary of £{calculate_net_salary(gross_salary, tax) : .2f}")

# Kelly Scott - 70311205