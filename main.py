from tkinter import*
from tkinter import messagebox
from datetime import datetime
import csv
import os

expenses = []
def add_click(): # Function for add click button
    add_window=Toplevel()
    add_window.title("Add New Expense")

    Label(add_window, text="Description:").pack(pady=5)
    desc_entry = Entry(add_window, width=30)
    desc_entry.pack(pady=5)

    Label(add_window, text="Amount:").pack(pady=5)
    amount_entry = Entry(add_window, width=30)
    amount_entry.pack(pady=5)

    Label(add_window, text="Date (Optional):").pack(pady=5)
    date_entry = Entry(add_window, width=30)
    date_entry.pack(pady=5)

    def save_expense():
        desc = desc_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()

        if not desc or not amount:
                messagebox.showwarning("Input Error", "Please fil in description and amount.")
                return
        
        if not date: # Adding today's date if date is empty
             date = datetime.today().strftime("%Y-%m-%d")

        try:
            amount = float(amount)
        except ValueError:
             messagebox.showerror("Input Error", "Amount must be a number.")
             return

        expenses.append({"desc": desc, "amount": amount, "date": date})
        messagebox.showinfo("Success", "Expense added!")
        add_window.destroy()

    Button(add_window, text="Save", command=save_expense).pack(pady=15)

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
