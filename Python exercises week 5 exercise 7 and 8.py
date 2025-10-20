import random

fruits = ["apple", "banana", "mango", "orange", "grape", "pear"]
score = 0
rounds = 0

while True:
    random_index = random.randint(0, len(fruits) - 1)
    chosen_fruit = fruits[random_index]

    guess = input("Type your guess fruit: ").lower()
    rounds += 1

    if guess == chosen_fruit:
        print("Your guess fruit is correct!")
        score += 1
    else:
        print(f"Your guess fruit is wrong! The correct fruit was '{chosen_fruit}'.")

    again = input("Type your response, 1 to play again or 2 to quit: ")

    if again == "2":
        print(f"Total score {score} out of {rounds}")
        break
    
questions = [
    ["What keyword is used to define a function in Python?", "def"],
    ["Which data type is used to store True or False?", "bool"],
    ["What symbol is used for comments in Python?", "#"],
    ["What function is used to get input from user?", "input"],
    ["Which keyword is used to start a loop?", "for"],
    ["What is the output of print(2**3)?", "8"],
    ["What keyword stops a loop?", "break"],
    ["Which built-in function gives the length of a list?", "len"],
    ["What data type are values inside quotes?", "string"],
    ["What is the extension for Python files?", ".py"]
]

score = 0

for q in questions:
    answer = input(q[0] + " ").strip().lower()
    if answer == q[1]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {q[1]}")

print("\nYour total score:", score, "out of", len(questions))
