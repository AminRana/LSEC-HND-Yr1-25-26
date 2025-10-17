# Kelly Scott - 70311205

import random

fruits = ["apple", "pear", "mango", "strawberry", "raspberry", "orange", "banana"]

def fruits_string() -> str:
    final = ""
    for fruit in fruits:
        if fruits[-1] == fruit:
            final += fruit
        else:
            final += fruit + ", "
    return final


continue_playing = True

total = 0
total_correct = 0

while continue_playing:
    total += 1
    print(f"Possible fruits: {fruits_string()}")

    choice = random.choice(fruits)

    guess = input("Enter your guess: ")

    if guess.lower() == choice:
        print("Correct!")
        total_correct += 1
    else:
        print("Wrong, the fruit was " + choice + "!")

    print("Press 1 to continue playing, 2 to quit\n")
    user_input = int(input())

    if user_input == 2:
        continue_playing = False
        print(f"You scored {total_correct}/{total}! Goodbye!")

# Kelly Scott - 70311205