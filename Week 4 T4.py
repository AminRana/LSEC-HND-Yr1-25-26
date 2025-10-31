#Grade system calculator
 
score = int(input("Enter your marks please"))

if score > 74:
    print("Grade: Distinction, Excellent !")
elif score > 60:
    print("Grade: Merit, Welldone !")
elif score > 40:
    print("Grade : Pass, Nice !")
elif score > 0:
    print("Grade : Fail,")
else:
    print("Invalid mark has been entered, please enter between 0-100.")

a = input("Enter first value: ")
b = input("Enter second value: ")

if a.isdigit() and b.isdigit():           # OUTER type check (integers only)
    a = int(a)
    b = int(b)
    total = a + b
    print("Total:", total)
    if total < 100:
        print("Total is less than 100")
    else:
        print("Total is 100 or more")
else:
    print("Both inputs must be whole numbers.")

#Word length checker
word = input("Type a word: ")
length = len(word)

if length >= 1 and length <= 3:
    print("Too short word")
elif length >= 4 and length <= 8:
    print("Small word")
elif length >= 9 and length <= 12:
    print("Big word")
else:
    print("Too big word")
#Menu selection: 
print("1. Add")
print("2. Search")
print("3. Update")
print("4. Delete")

choice = int(input("Type a number between 1 and 4: "))

if choice == 1:
    print("Added")
elif choice == 2:
    print("Searched")
elif choice == 3:
    print("Updated")
elif choice == 4:
    print("Deleted")
else:
    print("Invalid choice")


#Profession rate

profession = input("Enter profession(teacher, doctor, lawyer, driver):").lower()

if profession == "teacher":
 print("Hourly rate = £25")
elif profession == "doctor":
 print("Hourly rate = £60")
elif profession == "lawyer":
 print("Hourly rate = £200")
elif profession == "driver":
 print("Hourly rate == £15")
else:
 print("Invalid, proffesion not found.")
print("1. Add\n2. Search\n3. Update\n4. Delete")
choice_str = input("Type a number (1-4): ")

if choice_str.isdigit():                  # OUTER: numeric?
    choice = int(choice_str)
    if 1 <= choice <= 4:                  # still OUTER: in range?
        # INNER: do the action
        if choice == 1:
            print("Added")
        elif choice == 2:
            print("Searched")
        elif choice == 3:
            print("Updated")
        else:
            print("Deleted")
    else:
        print("Number must be between 1 and 4.")
else:
    print("Please enter a number, not text.")

 # Yearly tax calulator

salary = float(input("Enter your yearly gross salary >"))

if salary <= 12570:
   tax_rate = 0 
elif salary <= 50270:
   tax_rate = 0.20
elif salary <= 12514040:
   tax_rate = 0.40
else:
   tax_rate = 0.45
   print("Too rich")

tax_amount = salary*tax_rate
net_salary =salary -tax_amount

print("Tax rate:", tax_rate * 100, "%")
print("Tax amount: £", round(tax_amount, 2))
print("Net salary: £", round(net_salary, 2))

#Random code generator 

import random

while True:
    secret = random.randint(1, 5)
    guess_str = input("Guess a number (1-5): ")

    if not guess_str.isdigit():
        print("Not a number. Stopping.")
        break

    guess = int(guess_str)

    if guess == secret:
        print("Correct! Let's go again...\n")
        # loop continues
    else:
        print(f"Wrong! The number was {secret}. Stopping.")
        break


#Odd and even numbers with range <
                                 -
n_str = input("Enter a number (0-100): ")

if n_str.isdigit():                        # OUTER: numeric?
    n = int(n_str)
    if 0 <= n <= 100:                      # OUTER: in range?
        # INNER: odd/even
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Number must be between 0 and 100.")
else:
    print("Please enter a whole number.")

   
