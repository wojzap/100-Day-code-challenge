from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

def button_clicked():
    print("i got clicked")
    text = input.get()
    my_label.config(text=text)

button = Button(text="I'm a button", command=button_clicked)
button.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=2, column=3)

new_button = Button(text="Second button")
new_button.grid(row=0, column=2)

window.mainloop()