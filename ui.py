from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

BACKGROUND = "#5B5656"
FOREGROUND = "#4D4646"
TEXT_COLOR = "#F5EAEA"
FONT = ("Arial", 18, "bold")
SCORE_FONT = ("Arial", 12, "bold")


class Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=BACKGROUND)

        self.score_label = Label(background=BACKGROUND, highlightthickness=0, fg="white")
        self.score_label.config(text=f"Score: 0", font=SCORE_FONT)
        self.score_label.grid(padx=20, pady=20, row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background=FOREGROUND, highlightthickness=0)
        self.question_label = self.canvas.create_text(150, 125, font=FONT, fill=TEXT_COLOR, width=280)
        self.canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)

        self.check_img = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=self.check_img, highlightthickness=0, command=self.check_pressed)
        self.check_button.grid(padx=20, pady=20, row=2, column=0)

        self.cross_img = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=self.cross_img, highlightthickness=0, command=self.cross_pressed)
        self.cross_button.grid(padx=20, pady=20, row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background=FOREGROUND)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text="You have reached the end of the Quiz")
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")

    def check_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def cross_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, func=self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
