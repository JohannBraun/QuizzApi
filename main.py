from question_model import Question
from quiz_brain import QuizBrain
from ui import Ui

import requests
import html

question_bank = []
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()

for question in question_data["results"]:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(type(question_bank))
print(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = Ui(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
