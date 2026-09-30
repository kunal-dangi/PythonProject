from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


window = Tk()
window.title("Quizzler")
window.config(padx=50, pady=50, bg="#385766")


score_label = Label(text="Score: 0", fg="white", bg="#385766", font=("Helvetica", 18, "bold"))
score_label.grid(column=1, row=0, pady=(0, 30))



canvas = Canvas(width=580, height=400, bg="white", highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=2, pady=20)


question_text = canvas.create_text(290, 200, text="", fill="#52636D", font=("Helvetica", 22, "bold", "italic"), width=500)



true_button = Button(text="✓", font=("Helvetica", 55, "bold"), fg="white", bg="#25B978", activebackground="#25B978", width=3, height=1, borderwidth=0, command=lambda: check_answer("True"))
true_button.grid(column=0, row=2, pady=30)



false_button = Button(text="✕", font=("Helvetica", 55, "bold"), fg="white", bg="#F2605D", activebackground="#F2605D", width=3, height=1, borderwidth=0, command=lambda: check_answer("False"))
false_button.grid(column=1, row=2, pady=30)



def next_question():
    if quiz.still_has_questions():
        quiz.current_question = quiz.question_list[quiz.question_number]
        quiz.question_number += 1

        q_text = quiz.current_question.text

        canvas.itemconfig(question_text, text=q_text)
        score_label.config(text=f"Score: {quiz.score}")
    else:
        canvas.itemconfig(question_text, text="You've completed the quiz!")
        true_button.config(state="disabled")
        false_button.config(state="disabled")



def check_answer(user_answer):
    quiz.check_answer(user_answer)
    score_label.config(text=f"Score: {quiz.score}")
    next_question()


next_question()

window.mainloop()