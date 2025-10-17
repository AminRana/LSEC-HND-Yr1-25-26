# Kelly Scott - 70311205

quiz = [
    {"question": "How many legs does a cat have?", # 1
    "choices": [
        "1. 4 legs",
        "2. 6 legs",
        "3. 100 legs",
        "4. 3 legs"],
    "correct_answer": 0},

    {"question": "What is a cat's favourite food?", # 2
     "choices": [
         "1. Chocolate",
         "2. Fish",
         "3. Cabbage",
         "4. Peanuts"],
     "correct_answer": 1},

    {"question": "How many cat's is acceptable to own?", # 3
     "choices": [
         "1. 7 cats",
         "2. 1 cat",
         "3. 3 cats",
         "4. Anything below 1000"],
     "correct_answer": 3},

    {"question": "What is the best animal?", # 4
     "choices": [
         "1. Cat",
         "2. Dog",
         "3. Dragon",
         "4. Dolphin"],
     "correct_answer": 2},

    {"question": "Why is a dragon cooler than a cat?", # 5
     "choices": [
         "1. It's not, that was a trick question.",
         "2. Because dragon's are not real, and that's so cool",
         "3. Cats suck!",
         "4. They fly"],
     "correct_answer": 0},

    {"question": "If you could become a cat, would you?", # 6
     "choices": [
         "1. Yes",
         "2. No",
         "3. Maybe",
         "4. Never"],
     "correct_answer": 0},

    {"question": "What do cats like to drink?", # 7
     "choices": [
         "1. Milk",
         "2. Water",
         "3. Orange juice",
         "4. Apple juice"],
     "correct_answer": 1},

    {"question": "Which of these is not a cat?", # 8
     "choices": [
         "1. Tiger",
         "2. Cat",
         "3. Leopard",
         "4. Not a cat"],
     "correct_answer": 3},

    {"question": "Which of these is a cat?", # 9
     "choices": [
         "1. Dog",
         "2. Shark",
         "3. Lion",
         "4. Dolphin"],
     "correct_answer": 2},

    {"question": "How many lives do cats have?", # 10
     "choices": [
         "1. 1",
         "2. 3",
         "3. 9",
         "4. 2"],
     "correct_answer": 2}
]

points = 0

for quiz_part in quiz:
    print(quiz_part["question"])
    for choice in quiz_part["choices"]:
        print(choice)
    print("~~~~~~~~~~~~")
    player_answer = int(input())

    if player_answer - 1 == quiz_part["correct_answer"]:
        print("Correct!")
        points += 1
    else:
        print(f"Incorrect, the correct answer was {quiz_part["correct_answer"] + 1}")

print(f"Your total score was {points}/{len(quiz)}")


# Kelly Scott - 70311205