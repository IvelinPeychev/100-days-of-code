class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: '
                       f'{question.question} (True/False)?: ')

        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')


