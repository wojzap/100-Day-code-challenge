from tkinter import *
from tkinter import messagebox
import pandas
import random
import os


BACKGROUND_COLOR = "#B1DDC6"

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")

current_card = {}
words_to_learn = {}

# Picking random word
def pick_random_word():
    global current_card, flip_card_timer
    window.after_cancel(flip_card_timer)
    if len(to_learn) == 0:
        os.remove('data/words_to_learn.csv')
        messagebox.showinfo(title="CONGRATULATIONS!", message="You have learned all words.")
        window.destroy()
    else:
        current_card = random.choice(to_learn)
        card_front_canvas.itemconfig(language_canvas_text, text="French", fill="black")
        card_front_canvas.itemconfig(word_canvas_text, text=current_card["French"], fill="black")
        card_front_canvas.itemconfig(card_canvas_image, image=card_front_image)
        flip_card_timer = window.after(3000, flip_card)


def flip_card():
    card_front_canvas.itemconfig(card_canvas_image, image=card_back_image)
    card_front_canvas.itemconfig(language_canvas_text, text="English", fill="white")
    card_front_canvas.itemconfig(word_canvas_text, text=current_card["English"], fill="white")

def save_progress():
    global words_to_learn
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        words_to_learn = pandas.DataFrame.from_records(to_learn)
        words_to_learn.to_csv("data/words_to_learn.csv", index=False)
        pick_random_word()
    else:
        messagebox.showinfo(title="CONGRATULATIONS!", message="You have learned all words.")
        window.destroy()


# UI config
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_card_timer = window.after(3000, flip_card)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")

right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=save_progress)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=pick_random_word)

card_front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas_image = card_front_canvas.create_image(400, 263, image=card_front_image)
language_canvas_text = card_front_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_canvas_text = card_front_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)
card_front_canvas.grid(row=0, column=0, columnspan=2)

pick_random_word()

window.mainloop()



