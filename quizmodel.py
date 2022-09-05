class QuizModel:
    def __init__(self,q_list):
      self.question_number=0
      self.question_list=q_list
      self.score=0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:

            return False
    def next_question(self):
      currtent_question =self.question_list[self.question_number]
      self.question_number+=1
      user_answer=input(f"Q.{self.question_number} {currtent_question.text}\n Enter your answer:(a,b,c or d):  ")
      self.check_answer(user_answer, currtent_question.answer)
    def check_answer(self,user_answer,correct_answer):

        if user_answer.lower()==correct_answer.lower():
            self.score+=1

        else:
            self.score -= 1

        print("\n")