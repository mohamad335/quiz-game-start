class QuizBrain:
    score = 0
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number =0
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q{self.question_number}: {current_question} (True/False): ")
        self.next_answer(user_answer, current_question.answer)

    def next_answer(self,user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score +=1

        else:
            print("That's wrong.")
        print(f"the correct answer is {correct_answer}")
        print(f"your current score: {self.score}/{self.question_number}")
        print("\n")



