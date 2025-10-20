colours = ['red, green, red, blue, yellow,pink, blue, green, blue, white']
print (colours)
user_colour = input("enter colour to count: ").lower()
count = colours.count(user_colour)
print(f"The Colour '{user_colour}' appears{count} times.")

items = ['apple', 'banana', 'cherry']

while True:
    print("\nMenu:")
    print("1. Display list")
    print("2. Add item")
    print("3. Delete item")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current list:", items)

    elif choice == "2":
        new_item = input("Enter item to add: ")
        items.append(new_item)
        print(f"'{new_item}' added.")

    elif choice == "3":
        del_item = input("Enter item to delete: ")
        if del_item in items:
            items.remove(del_item)
            print(f"'{del_item}' deleted.")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

