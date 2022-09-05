from questionmodel import Question
from QUESTIONS import question_data
from quizmodel import QuizModel
print("This is a MYSQL quiz ,which contains 10 questions \n You have to get at least 5 of 10 to pass this quiz.\n GOOD LUCK:)")
fname=input("Enter your first name: ")
lname=input("Enter your last name:")
sid=input(" Enter your student's number:")
question_bank = []
for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]
    new_question =Question(question_text, question_answer)
    question_bank.append(new_question)
    quiz = QuizModel(question_bank)
while quiz.still_has_question():
     quiz.next_question()
print("You have completed the quiz")
print(f"your final score is : {quiz.score}/{quiz.question_number}")