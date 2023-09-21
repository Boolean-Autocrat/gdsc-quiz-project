from quiz.question import Question
from colorama import init, Fore, Back, Style
from quiz.welcome_art import welcome_text
import time
import random


class QuizManager:
    def __init__(self, question_data):
        self.questions = [Question(q) for q in question_data]
        random.shuffle(self.questions)
        self.score = 0
        init(autoreset=True)
        self.current_question_index = 0

    def load_question(self):
        print("-" * 20)
        current_q = self.questions[self.current_question_index]
        start_time = time.time()
        answer = input(
            f"Question {current_q.question_text} {Fore.GREEN + '(true' '/' + Fore.RED + 'false)' + Fore.WHITE + ': '}"
        )
        end_time = time.time()
        print("Time taken: ", round((end_time - start_time), 2), "s")
        if (answer.lower() != "true") and (answer.lower() != "false"):
            print(Style.BRIGHT + Back.WHITE + Fore.BLUE + "Skipped question!")
            current_q.status = "skipped"
        elif self.check_answer(answer.title(), current_q):
            self.score += 2
            print(Style.BRIGHT + Back.WHITE + Fore.GREEN + "Correct!")
            current_q.status = "correct"
        else:
            self.score -= 1
            print(Style.BRIGHT + Back.WHITE + Fore.RED + "Incorrect!")
            current_q.status = "incorrect"
        print()
        self.display_options()
        self.current_question_index += 1
        print("-" * 20)

    def timer(self):
        time.sleep(self.timeout_duration)

    def start_quiz(self):
        print(Style.BRIGHT + Back.WHITE + Fore.BLUE + welcome_text, end="\n")
        print(
            "Da Rules: \n1. The questions are true/false.\n2. After spending >= 20 seconds on a single question, 1 point will be deducted.\n3. Follow the instructions on screen and have fun!\n4. Entering anything other than true/false will skip the question (0 points).\n"
        )
        input("Press any key to start the quiz...")
        self.load_question()

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def display_options(self):
        options = ["A. Next Question", "B. Previous Question", "C. Submit Quiz"]
        if self.current_question_index == 0:
            options.remove("B. Previous Question")
        if self.current_question_index == len(self.questions) - 1:
            options.remove("A. Next Question")
        for option in options:
            print(option)
        option = input("Select an option: ")
        if option.upper() == "A":
            self.next_question()
        elif option.upper() == "B":
            self.previous_question()
        elif option.upper() == "C":
            self.submit_quiz()
        else:
            print("Invalid option!")
            print("-" * 20)
            self.display_options()

    def check_answer(self, answer, question):
        return answer == question.answer

    def next_question(self):
        self.current_question_index += 1
        if self.questions[self.current_question_index].status == "unattempted":
            self.load_question()
            return
        self.display_question_summary()

    def previous_question(self):
        self.current_question_index -= 1
        self.display_question_summary()

    def display_question_summary(self):
        current_question = self.questions[self.current_question_index]
        print("-" * 20)
        print(f"Q: {current_question.question_text}")
        print(
            f"Correct Answer: {current_question.answer}; Player Status: {current_question.status}"
        )
        print("-" * 20)
        self.display_options()

    def display_question(self):
        current_question = self.questions[self.current_question_index]
        print(f"Q: {current_question.question_text}")
        print(f"Your answer: {current_question.answer} - {current_question.status}")

    def submit_quiz(self):
        print("-" * 20)
        print(f"Your score is {Fore.GREEN + str(self.score) + Fore.WHITE}.")
        print(Style.BRIGHT + Back.WHITE + Fore.CYAN + "Thanks for playing!")
        exit()
