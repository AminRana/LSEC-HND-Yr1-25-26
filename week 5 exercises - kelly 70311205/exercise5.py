# Kelly Scott - 70311205

user_list = []

def create_list():
    global user_list

    new_item = str(input("Add another item (-1 to stop): "))

    if new_item != "-1":
        user_list.append(new_item)

    while new_item != "-1":
        new_item = str(input("Add another item (-1 to stop): "))

        if new_item != "-1":
            user_list.append(new_item)

create_list()

count = len(user_list)

if count > 1:
    print(f"Your list has {count} items!")
else:
    print(f"Your list has {count} item!")

# Kelly Scott - 70311205