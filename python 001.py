

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0


    def search_answer(self, user_answer, valid_answers):
        for item in valid_answers:
            if item == user_answer:
                return True
        return False

    def ask_questions(self):
        print("\n--- Welcome to the Quiz Game! ---\n")

        for q in self.questions:
            print(q.prompt)

            user_answer = input("Your answer: ").strip().lower()

            
            valid_inputs = ["a", "b", "c", "d"]
            while not self.search_answer(user_answer, valid_inputs):
                print("Invalid input! Please enter A, B, C or D.")
                user_answer = input("Your answer: ").strip().lower()

            if user_answer == q.answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer was: {q.answer.upper()}\n")

        self.show_results()

    def show_results(self):
        print("-----------------------------------")
        print(f"Quiz Complete! Your Score: {self.score}/{len(self.questions)}")

        if self.score == len(self.questions):
            print("Excellent! You got everything right!")
        elif self.score > len(self.questions) / 2:
            print("Good job! You passed.")
        else:
            print("Keep practicing! You can do better.")
        print("-----------------------------------")



question_prompts = [
    "1. What is the capital of France?\nA. Madrid\nB. Paris\nC. Rome\nD. Berlin\n",
    "2. Which number is even?\nA. 3\nB. 7\nC. 10\nD. 9\n",
    "3. What does CPU stand for?\nA. Central Processing Unit\nB. Computer Personal Unit\nC. Central Power Utility\nD. Control Processing Unit\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]


quiz = QuizGame(questions)
quiz.ask_questions()
