class Question:
    def __init__(self, question):
        self.question_text = question["text"]
        self.answer = question["answer"]
        self.status = "unattempted"
