# Define the Question class. Objects of such class have two properties: text of a question and the correct answer.
# When created, two parameters shoud be provided, q_text and q_answer, which originate from

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
