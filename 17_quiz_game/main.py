from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

# this consists of a list of Question objects
question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

# creating the quiz object from the QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

