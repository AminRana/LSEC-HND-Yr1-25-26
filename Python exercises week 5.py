text = input("Enter a string: ")

for char in text:
    if char.lower() in "aeiou":
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")


total = 0
for num in range(2, 21, 2):
    total += num
print("Sum of even numbers up to 20:", total)

def add():
    print("Add selected")

def search():
    print("Search selected")

def update():
    print("Update selected")

def delete():
    print("Delete selected")

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

for num in range(2, 21):  # numbers from 2 to 20
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, "is a prime number")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



        
