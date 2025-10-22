import random

# List of fruits
fruits = ['apple', 'banana', 'mango', 'orange', 'grapes', 'pineapple', 'kiwi']

# Generate a random index
index = random.randint(0, len(fruits)-1)
selected_fruit = fruits[index]

# Let the user guess the fruit
guess = input("Guess the fruit: ").lower()

if guess == selected_fruit:
    print("Congratulations! You guessed it right!")
else:
    print(f"Oops! The correct fruit was '{selected_fruit}'.")


# Quiz questions and answers
quiz = {
    "What is the capital of France?": "paris",
    "Who wrote 'Romeo and Juliet'?": "shakespeare",
    "What is the largest planet in our solar system?": "jupiter",
    "What is 5 + 7?": "12",
    "Which element has symbol O?": "oxygen",
    "What is the boiling point of water in Celsius?": "100",
    "Who painted the Mona Lisa?": "da vinci",
    "What is the smallest prime number?": "2",
    "What is the chemical formula for water?": "h2o",
    "Who discovered gravity?": "newton"
}

score = 0

# Loop through each question
for question, answer in quiz.items():
    user_answer = input(question + " ").lower().strip()
    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is '{answer}'.\n")

print(f"Your total score is {score} out of {len(quiz)}")
