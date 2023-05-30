from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for questions in question_data:
    question = Question(questions['text'], questions['answer'])
    question_bank.append(question)

# print(question_bank[0].question)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()


print('You complete the quiz!')
print(f'Your final score is {quiz.score} / {quiz.question_number}')

