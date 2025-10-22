# program to check vowels in a string.

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

# Iterate characters one by one.
for ch in text:
    if ch in vowels:
        print(ch, "is a vowel.")
    else:
        print(ch, "is not a vowel.")


# program to add even numbers up to 20 using while loop.

total = 0
i = 2

while i <= 20:
    total += i
    i += 2

print("The sum of even numbers up to 20 is:", total)

# Menu-driven program.

while True:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. search")
    print("3. Update")
    print("4. Delete")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("You selected Add.")
    elif choice == "2":
        print("You selected Search.")
    elif choice == "3":
        print("You selected Update:")
    elif choice == "4":
        print("You selected Delete.")
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
    
