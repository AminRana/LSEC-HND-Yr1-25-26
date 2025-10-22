# Initial list
items = ['apple', 'banana', 'cherry']

while True:
    print("\nMenu:")
    print("1 - Display items")
    print("2 - Add item")
    print("3 - Delete item")
    print("4 - Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Items:", items)
    elif choice == '2':
        new_item = input("Enter item to add: ")
        items.append(new_item)
        print(f"'{new_item}' added.")
    elif choice == '3':
        del_item = input("Enter item to delete: ")
        if del_item in items:
            items.remove(del_item)
            print(f"'{del_item}' deleted.")
        else:
            print(f"'{del_item}' not found.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
