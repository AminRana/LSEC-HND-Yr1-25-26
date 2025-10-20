# ========= 3a =========
mark = int(input("3a) Enter mark 0-100: "))
if mark > 74:
    print("Grade: Distinction")
elif 60 <= mark <= 74:
    print("Grade: Merit")
elif 40 <= mark <= 59:
    print("Grade: Pass")
elif 0 <= mark <= 39:
    print("Grade: Fail")
else:
    print("Invalid mark")

# ========= 3b =========
text = input("3b) Enter a word: ")
n = len(text)
if 1 <= n <= 3:
    print("too short word")
elif 4 <= n <= 8:
    print("small word")
elif 9 <= n <= 12:
    print("big word")
elif n > 12:
    print("too big word")
else:
    print("empty input")

# ========= 3c =========
print("3c) Menu")
print("1. Add")
print("2. Search")
print("3. Update")
print("4. Delete")
choice = int(input("Type 1-4: "))
if choice == 1:
    print("Added")
elif choice == 2:
    print("Searched")
elif choice == 3:
    print("Updated")
elif choice == 4:
    print("Deleted")
else:
    print("Invalid option")

# ========= 3d =========
rates = {
    "teacher": 25,
    "doctor": 60,
    "lawyer": 200,
    "driver": 15,
}
prof = input("3d) Type a profession (teacher, doctor, lawyer, driver): ").strip().lower()
if prof in rates:
    print(f"Hourly rate: £{rates[prof]}")
else:
    print("Unknown profession")

# ========= 3e =========
# Uses a single tax rate by band (as the exercise states)
gross = float(input("3e) Enter yearly gross salary (£): "))
if gross <= 12570:
    rate = 0.00
elif gross <= 50270:
    rate = 0.20
elif gross <= 125140:
    rate = 0.40
else:
    rate = 0.45

tax = gross * rate
net = gross - tax
print(f"Tax rate: {int(rate*100)}%")
print(f"Tax: £{tax:.2f}")
print(f"Net salary: £{net:.2f}")
