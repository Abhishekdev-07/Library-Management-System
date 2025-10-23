import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import mysql.connector

# MySQL Connection Setup
con = mysql.connector.connect(
    host='localhost',
    user='root',
    charset='utf8mb4',
    password='querying_through_a_mine123$USA',
    database='CSProject'
)
cur = con.cursor()

# Main Window Setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x500")

# Main Frame for Scrollable Content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Enable Scrolling with Mouse Wheel
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas = tk.Canvas(main_frame)
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel) # Mouse wheel scrolling

scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


### Utility Functions ###

def clear_screen():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

def clear_entries(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)


### Insert Book Screen ###

def insert_book_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Insert Book", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    fields = [
        ("Book ID", 1), ("Book Name", 2), ("Publication Date", 3), ("Author", 4), 
        ("Publisher", 5), ("Price", 6), ("Book Type", 7), ("Quantity", 8)
    ]
    entries = {}
    
    for label, row in fields:
        tk.Label(scrollable_frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(scrollable_frame)
        entry.grid(row=row, column=1)
        entries[label] = entry

    def insert_book_action():
        try:
            book_data = [
                int(entries["Book ID"].get()), entries["Book Name"].get(), 
                entries["Publication Date"].get(), entries["Author"].get(), 
                entries["Publisher"].get(), int(entries["Price"].get()), 
                entries["Book Type"].get(), int(entries["Quantity"].get())
            ]
            sql = "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, book_data)
            con.commit()
            messagebox.showinfo("Success", "Book inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Insert", command=insert_book_action).grid(row=9, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: clear_entries(entries)).grid(row=9, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu, columnspan=2, pady=10).grid(row=10, column=0, columnspan=2, pady=10)


### Insert Student Screen ###

def insert_student_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Insert Student", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)

    fields = [
        ("Name", 2), ("Registration ID", 3), ("Address", 4), ("Course", 5), 
        ("Account Number", 6), ("Gender", 7)
    ]
    entries = {}
    
    for label, row in fields:
        tk.Label(scrollable_frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(scrollable_frame)
        entry.grid(row=row, column=1)
        entries[label] = entry

    def insert_student_action():
        try:
            student_data = [
                entries["Name"].get(), entries["Registration ID"].get(), 
                entries["Address"].get(), entries["Course"].get(), 
                entries["Account Number"].get(), entries["Gender"].get()
            ]
            sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(sql, student_data)
            con.commit()
            messagebox.showinfo("Success", "Student record inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Insert", command=insert_student_action).grid(row=8, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: clear_entries(entries)).grid(row=8, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu, columnspan=2, pady=10).grid(row=9, column=0, columnspan=2, pady=10)


### Issue Book Screen ###

def issue_book_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Issue Book", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    fields = [
        ("Registration ID", 1), ("Book ID", 2), ("Issue Date", 3), ("Return Date", 4), 
        ("Account Number", 5), ("Issue Name", 6), ("Course", 7), ("Volume", 8), ("Edition", 9)
    ]
    entries = {}
    
    for label, row in fields:
        tk.Label(scrollable_frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(scrollable_frame)
        entry.grid(row=row, column=1)
        entries[label] = entry

    def issue_book_action():
        try:
            issue_data = [
                entries["Registration ID"].get(), entries["Book ID"].get(), 
                entries["Issue Date"].get(), entries["Return Date"].get(), 
                entries["Account Number"].get(), entries["Issue Name"].get(), 
                entries["Course"].get(), entries["Volume"].get(), entries["Edition"].get()
            ]
            sql = "INSERT INTO issue VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, issue_data)
            con.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Issue Book", command=issue_book_action).grid(row=10, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: clear_entries(entries)).grid(row=10, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu, columnspan=2, pady=10).grid(row=11, column=0, columnspan=2, pady=10)


### Return Book Screen ###

def return_book_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Return Book", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)

    fields = [("Registration ID", 1), ("Return Date (YYYY-MM-DD)", 2)]
    entries = {}
    
    for label, row in fields:
        tk.Label(scrollable_frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(scrollable_frame)
        entry.grid(row=row, column=1)
        entries[label] = entry

    def return_book_action():
        try:
            regno = entries["Registration ID"].get()
            return_date = entries["Return Date (YYYY-MM-DD)"].get()
            
            sql = """
SELECT i.bookid, i.date_of_issue_books, i.date_of_return_books, b.price
FROM issue i
JOIN books b ON i.bookid = b.bookid
WHERE i.regno = %s
"""
            cur.execute(sql, (regno,))
            result = cur.fetchone()
            cur.fetchall() # to clear any data and to ensure no errors come

            if result:
                bookid, issue_date_str, due_date_str, price = result
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
                
                # Assuming issue date and due date are stored in the issue table.
                # The PDF code only uses due_date_str, so we adjust slightly for safety.
                # Assuming 'date_of_return_books' in the DB is the original 'due date'
                
                if datetime.strptime(return_date, '%Y-%m-%d').date() > due_date:
                    # Calculate fine (if needed, but PDF just shows 'Late Fine: ₹{result[3]}')
                    messagebox.showinfo("Late Return", f"Book returned late! Fine: ₹{price}")
                else:
                    messagebox.showinfo("On Time", "Book returned on time.")

                # Delete the issue record
                cur.execute("DELETE FROM issue WHERE regno = %s", (regno,))
                con.commit()
                messagebox.showinfo("Success", "Book returned successfully!")
            else:
                messagebox.showinfo("Error", "No records found.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Return Book", command=return_book_action).grid(row=3, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: clear_entries(entries)).grid(row=3, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu).grid(row=4, column=0, columnspan=2, pady=10)


### Search Issued Books Screen ###

def search_issued_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Search Issued Books", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    tk.Label(scrollable_frame, text="Book ID").grid(row=1, column=0)
    book_id_entry = tk.Entry(scrollable_frame)
    book_id_entry.grid(row=1, column=1)

    def search_issued_action():
        try:
            book_id = book_id_entry.get()
            
            sql = """
SELECT s.Bookid, s.Name, s.Regno, s.Gender, i.Date_of_issue_books, i.Date_of_return_books
FROM student s
JOIN issue i ON s.Regno = i.Regno
WHERE i.Bookid = %s
"""
            cur.execute(sql, (book_id,))
            results = cur.fetchall()

            if results:
                result_str = "\n".join([str(row) for row in results])
                messagebox.showinfo("Search Results", result_str)
            else:
                messagebox.showinfo("No Records", f"No records found for Book ID: {book_id}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Search Issued", command=search_issued_action).grid(row=2, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: book_id_entry.delete(0, tk.END)).grid(row=2, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu, columnspan=2, pady=10).grid(row=3, column=0, columnspan=2, pady=10)


### Remove Student Screen ###

def remove_student_screen():
    clear_screen()
    tk.Label(scrollable_frame, text="Remove Student", font=('Arial', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    fields = [("Registration ID", 1), ("Name", 2)]
    entries = {}
    
    for label, row in fields:
        tk.Label(scrollable_frame, text=label).grid(row=row, column=0)
        entry = tk.Entry(scrollable_frame)
        entry.grid(row=row, column=1)
        entries[label] = entry

    def remove_student_action():
        try:
            regno = entries["Registration ID"].get()
            name = entries["Name"].get()
            
            sql = "DELETE FROM student WHERE regno = %s AND name = %s"
            cur.execute(sql, (regno, name))
            con.commit()
            messagebox.showinfo("Success", "Student removed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    tk.Button(scrollable_frame, text="Remove Student", command=remove_student_action).grid(row=3, column=0, pady=10)
    tk.Button(scrollable_frame, text="Clear", command=lambda: clear_entries(entries)).grid(row=3, column=1, pady=10)
    tk.Button(scrollable_frame, text="Exit", command=show_main_menu, columnspan=2, pady=10).grid(row=4, column=0, columnspan=2, pady=10)


### Main Menu UI ###

def show_main_menu():
    clear_screen()
    tk.Label(scrollable_frame, text="Library Management System", font=('Arial', 16, 'bold')).pack(pady=20)
    
    buttons = [
        ("Insert Book", insert_book_screen),
        ("Insert Student", insert_student_screen),
        ("Issue Book", issue_book_screen),
        ("Return Book", return_book_screen),
        ("Search Issued Books", search_issued_screen),
        ("Remove Student", remove_student_screen)
    ]
    
    for text, command in buttons:
        tk.Button(scrollable_frame, text=text, command=command, width=20, height=2).pack(pady=20, padx=100, anchor="center")


### Initial Display ###

show_main_menu()
root.mainloop()
