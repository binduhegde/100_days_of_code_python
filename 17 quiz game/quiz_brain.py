class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    # returns true if there are any questions left and false otherwise
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # asks the next question and triggers the check_answer function
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # because the question number starts from 0, we're updating it here and now
        # so that while taking input, the question number is right. (fixes the 0 indexed prob)
        self.question_number += 1
        inp = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(inp, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right 💫")
            self.score += 1
        else:
            print(f"That is wrong! The right answer was {correct_answer} 😐")
        # doesn't get executed if it is the last question because it has to say 'final score'
        # not current score. else will handle it
        if self.question_number != len(self.question_list):
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print(f"\nYou've completed the quiz 🎊\nYour final score is: {self.score}/{len(self.question_list)} 🎖️")


        
