from question import Question
from data import question_data
from brain import QuestionBrain

question_bank= []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuestionBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Quiz is completed")
print(f"Your Final Score is {quiz.score}/{quiz.question_number}")
