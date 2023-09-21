from quiz.quiz_manager import QuizManager
from data.questions import question_data


def main():
    quiz_manager = QuizManager(question_data)
    quiz_manager.start_quiz()


if __name__ == "__main__":
    main()
