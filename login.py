import tkinter as tk
from tkinter import messagebox
import re

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application")
        self.root.configure(bg="white")  # Set background color

        # Create a frame for the options
        options_frame = tk.Frame(root, bg="white", pady=20)
        options_frame.pack(side=tk.TOP)

        # Create a label for selecting the choice with a blue background
        label = tk.Label(options_frame, text="Select Your Choice:", font=("Helvetica", 14), bg="#3498db", fg="white", pady=10)
        label.pack()

        # Create buttons for Login and Register options with padding
        tk.Button(options_frame, text="Login", command=self.show_login_window, padx=10, pady=5, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(options_frame, text="Register", command=self.show_register_window, padx=10, pady=5, font=("Helvetica", 12)).pack(pady=5)

    def show_login_window(self):
        # Create a new window for the login functionality with a title
        login_window = tk.Toplevel(self.root)
        login_window.title("Login - Please Enter Your Details")

        # Create a header label for the login window
        tk.Label(login_window, text="Login", font=("Helvetica", 16)).pack(pady=10)

        # Create variables for user ID and password
        self.user_id_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Create labels and entry widgets for user ID and password with padding
        tk.Label(login_window, text="User ID (Email):", font=("Helvetica", 12)).pack(pady=5)
        user_id_entry = tk.Entry(login_window, textvariable=self.user_id_var, font=("Helvetica", 12))
        user_id_entry.pack(pady=5)

        tk.Label(login_window, text="Password:", font=("Helvetica", 12)).pack(pady=5)
        password_entry = tk.Entry(login_window, show="*", textvariable=self.password_var, font=("Helvetica", 12))
        password_entry.pack(pady=5)

        # Create a login button with padding
        tk.Button(login_window, text="Login", command=self.login, padx=10, pady=5, font=("Helvetica", 12)).pack(pady=10)

    def show_register_window(self):
        # Create a new window for the register functionality with a title
        register_window = tk.Toplevel(self.root)
        register_window.title("Register - Please Enter Your Details")

        # Create a header label for the register window
        tk.Label(register_window, text="Register", font=("Helvetica", 16)).pack(pady=10)

        # Create variables for user ID and password
        self.new_user_id_var = tk.StringVar()
        self.new_password_var = tk.StringVar()

        # Create labels and entry widgets for user ID and password with padding
        tk.Label(register_window, text="New User ID (Email):", font=("Helvetica", 12)).pack(pady=5)
        new_user_id_entry = tk.Entry(register_window, textvariable=self.new_user_id_var, font=("Helvetica", 12))
        new_user_id_entry.pack(pady=5)

        tk.Label(register_window, text="New Password:", font=("Helvetica", 12)).pack(pady=5)
        new_password_entry = tk.Entry(register_window, show="*", textvariable=self.new_password_var, font=("Helvetica", 12))
        new_password_entry.pack(pady=5)

        # Create a register button with padding
        tk.Button(register_window, text="Register", command=self.register, padx=10, pady=5, font=("Helvetica", 12)).pack(pady=10)

    def login(self):
        # Validate user ID and password
        user_id = self.user_id_var.get()
        password = self.password_var.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_id):
            messagebox.showerror("Error", "Invalid User ID (Email)")
            return

        if not (any(c.isdigit() for c in password) and any(c.isupper() for c in password)):
            messagebox.showerror("Error", "Invalid Password. Password should contain at least one digit and one capital letter.")
            return

        # Check user ID and password from file (replace with your file handling logic)
        valid_user_id = "test@example.com"
        valid_password = "Password123"

        if user_id == valid_user_id and password == valid_password:
            messagebox.showinfo("Login Successful", "Welcome, {}".format(user_id))
        else:
            messagebox.showerror("Login Failed", "Invalid User ID or Password")

    def register(self):
        # Validate new user ID and password
        new_user_id = self.new_user_id_var.get()
        new_password = self.new_password_var.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_user_id):
            messagebox.showerror("Error", "Invalid User ID (Email)")
            return

        if not (any(c.isdigit() for c in new_password) and any(c.isupper() for c in new_password)):
            messagebox.showerror("Error", "Invalid Password. Password should contain at least one digit and one capital letter.")
            return

        # Save new user ID and password to file (replace with your file handling logic)
        # In a real application, you should securely hash and store the password
        messagebox.showinfo("Registration Successful", "User registered successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()
