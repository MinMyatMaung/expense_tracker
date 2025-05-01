from tkinter import*
from tkinter import messagebox


def add_click():
    add_window=Toplevel()
    add_window.title("Add New Expense")

    Label(add_window, text="Description").pack(pady=5)
    date_entry = Entry(add_window, width=30)
    date_entry.pack(pady=5)


def view_click():
    print("view")

def summary_click():
    print("summary")
    
def exit_click():
    window.destroy()

window = Tk()
window.title("Expense Tracker")
add_button = Button(window, text="Add Expense")
add_button.config(command=add_click)

view_button = Button(window, text="View Expenses")
view_button.config(command=view_click)

summary_button = Button(window, text="View Summary")
summary_button.config(command=summary_click)

exit_button = Button(window, text="Exit")
exit_button.config(command=exit_click)

add_button.pack()
view_button.pack()
summary_button.pack()
exit_button.pack()
window.mainloop()
