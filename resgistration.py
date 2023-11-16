import tkinter as tk
from tkinter import messagebox
import csv
import re

def validate_mobile_number(mobile_number):
    # Validate mobile number using a simple regular expression
    return re.match(r'^\d{10}$', mobile_number)

def validate_email(email):
    # Validate email using a simple regular expression
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

def submit_form():
    # Get values from the entry widgets
    name = entry_name.get()
    mobile_number = entry_mobile.get()
    email = entry_email.get()
    terms_checked = var_terms.get()

    # Validate mobile number
    if not validate_mobile_number(mobile_number):
        messagebox.showerror("Error", "Invalid Mobile Number")
        return

    # Validate email
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid Email Address")
        return

    # Check if terms and conditions are checked
    if not terms_checked:
        messagebox.showerror("Error", "Please accept the Terms and Conditions")
        return

    # Store details in CSV file
    with open('student_details.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Mobile Number', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty and write header if necessary
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write student details
        writer.writerow({'Name': name, 'Mobile Number': mobile_number, 'Email': email})

    # Display success message
    messagebox.showinfo("Success", "Student details saved successfully")

    # Clear the entry widgets
    entry_name.delete(0, 'end')
    entry_mobile.delete(0, 'end')
    entry_email.delete(0, 'end')
    check_terms.deselect()

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create and pack widgets
label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_mobile = tk.Label(root, text="Mobile Number:")
label_mobile.pack()

entry_mobile = tk.Entry(root)
entry_mobile.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

var_terms = tk.BooleanVar()
check_terms = tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=var_terms)
check_terms.pack()

btn_submit = tk.Button(root, text="Submit", command=submit_form)
btn_submit.pack()

# Run the Tkinter event loop
root.mainloop()
