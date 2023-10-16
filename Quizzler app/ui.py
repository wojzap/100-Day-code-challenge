from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="question",
            width=280,
            font=("Arial", 20, "italic")
        )
        self.get_next_question()

        self.score = quiz.score
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.check_if_true
        )
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.check_if_false
        )

        self.score_text.grid(row=0, column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="No more questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def check_if_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
