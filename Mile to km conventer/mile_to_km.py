from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = miles_entry.get()
    result = round(int(miles) * 1.6)
    show_km_label.config(text=result)

calculate_button = Button(width=10, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

equal_label = Label(text="is equal to")
equal_label.grid(row=2, column=1)

show_km_label = Label(text=0)
show_km_label.grid(row=2, column=2)

miles_entry = Entry(width=10)
miles_entry.grid(row=1, column=2)


window.mainloop()