
import json
from tkinter import messagebox
import Openai_func
import openai
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Restaurant Review Generator")
window.geometry('800x500')

# Labels
name_label = Label(window, text="Name of Restaurant")
name_label.grid(column=0, row=0)
review_label = Label(window, text="Review of Restaurant")
review_label.grid(column=0, row=1)
output_label = Label(window, text="Generated Review")
output_label.grid(column=1, row=2)

# Entry
name_entry = Entry(window, width=50)
name_entry.grid(column=1, row=0)
review_entry = Entry(window, width=50)
review_entry.grid(column=1, row=1)
# output popup window



# Button
def clicked():
    name = name_entry.get()
    review = review_entry.get()
    output = Openai_func.generate(name, review)
    # generate messagge box from output
    messagebox.showinfo("Generated Review", output)


btn = Button(window, text="Generate", command=clicked)
btn.grid(column=1, row=3)

window.mainloop()