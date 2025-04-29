from tkinter import*
from tkinter import messagebox


def add_click():
    print("add")

def view_click():
    print("view")

def summary_click():
    print("summary")
    
def exit_click():
    print("exit")

window = Tk()
add_button = Button(window, text="Add Expense")
add_button.config(command=add_click)

view_button = Button(window, text="View Expenses")
view_button.config(command=view_click)

summary_button = Button(window, text="View Summary")
summary_button.config(command=summary_click)

exit_button = Button(window, text="Exit")
exit_button.config(command=exit_button)

add_button.pack()
view_button.pack()
summary_button.pack()
exit_button.pack()
window.mainloop()
