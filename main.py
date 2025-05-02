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

    Label(add_window, text="Date YYYY-MM-DD (Optional):").pack(pady=5)
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

        # Writing to CSV
        file_exists = os.path.isfile("expenses.csv")
        with open("expenses.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Description", "Amount", "Date"])
            writer.writerow([desc, amount, date])
        
        messagebox.showinfo("Success", "Expense added!")
        add_window.destroy()

    Button(add_window, text="Save", command=save_expense).pack(pady=15)

def view_click():
    view_window = Toplevel()
    view_window.title("View Expenses")
    view_window.geometry("400x300")

    scrollbar = Scrollbar(view_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(view_window, width=50, yscrollcommand=scrollbar.set)
    listbox.pack(pady=10, padx=10, fill=BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    # Reading from expenses.csv
    if not os.path.isfile("expenses.csv"):
         listbox.insert(END, "No expenses recroded yet.")
         return
    
    with open("expenses.csv", mode="r") as file:
         reader = csv.reader(file)
         for row in reader:
              if len(row) == 3:
                   desc, amount, date = row
                   listbox.insert(END, f"{date} | ${amount} | {desc}")

def summary_click():
    summary_window = Toplevel()
    summary_window.title("Summary")
    summary_window.geometry("300x150")

    total_expenses = 0.0
    expense_count = 0

    if not os.path.isfile("expenses.csv"):
         Label(summary_window, text="No expenses found.").pack(pady=20)
         return
    
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                _, amount, _ = row
                try:
                       total_expenses += float(amount)
                       expense_count += 1
                except ValueError:
                    continue
    Label(summary_window, text=f"Total Entries: {expense_count}", font=("Arial", 12)).pack(pady=10)
    Label(summary_window, text=f"Total Spent: ${total_expenses:.2f}", font=("Arial", 12, "bold")).pack(pady=5)
    
def exit_click():
    window.destroy()

window = Tk()
window.title("Expense Tracker")
add_button = Button(window, text="Add Expense")
add_button.config(command=add_click)

view_button = Button(window, text="View Expenses", command=view_click)

summary_button = Button(window, text="View Summary", command=summary_click)

exit_button = Button(window, text="Exit")
exit_button.config(command=exit_click)

add_button.pack()
view_button.pack()
summary_button.pack()
exit_button.pack()
window.mainloop()
