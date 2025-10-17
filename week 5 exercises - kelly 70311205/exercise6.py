# Kelly Scott - 70311205

menu = {
    1: ["Display", "Displayed"],
    2: ["Add", "Added"],
    3: ["Delete", "Deleted"],
    4: ["Update", "Updated"],
    5: ["Quit", "Bye!"]
}
for i in range(1, len(menu) + 1):
    print(f"{i}. {menu[i][0]}")

user_input = int(input())

print(menu[user_input][1])

while not user_input == 5:

    for i in range(1, len(menu) + 1):
        print(f"{i}. {menu[i][0]}")

    user_input = int(input())

    print(menu[user_input][1])

# Kelly Scott - 70311205