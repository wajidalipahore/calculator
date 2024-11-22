import tkinter as tk
from tkinter import messagebox

def perform_operation(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")

root = tk.Tk()
root.title("Simple Calculator - Bscys039")  # Replace "Your Roll Number" with the actual roll number
root.geometry("400x400")
root.config(bg="#e3f2fd")


title_label = tk.Label(root, text="Simple Calculator by wajid ali", font=("Arial", 16, "bold"), bg="red", fg="#333")
title_label.pack(pady=10)

entry_frame = tk.Frame(root, bg="red")
entry_frame.pack(pady=20)

entry1_label = tk.Label(entry_frame, text="Enter First Number:", font=("Arial", 12), bg="#e3f2fd", fg="#555")
entry1_label.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(entry_frame, font=("Arial", 12), width=15)
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2_label = tk.Label(entry_frame, text="Enter Second Number:", font=("Arial", 12), bg="#e3f2fd", fg="#555")
entry2_label.grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(entry_frame, font=("Arial", 12), width=15)
entry2.grid(row=1, column=1, padx=10, pady=5)


button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add", font=("Arial", 12), bg="#4caf50", fg="white", 
                        command=lambda: perform_operation("add"))
add_button.grid(row=0, column=0, padx=10)

subtract_button = tk.Button(button_frame, text="Subtract", font=("Arial", 12), bg="#f44336", fg="white", 
                             command=lambda: perform_operation("subtract"))
subtract_button.grid(row=0, column=1, padx=10)

multiply_button = tk.Button(button_frame, text="Multiply", font=("Arial", 12), bg="#2196f3", fg="white", 
                             command=lambda: perform_operation("multiply"))
multiply_button.grid(row=1, column=0, padx=10, pady=10)

divide_button = tk.Button(button_frame, text="Divide", font=("Arial", 12), bg="#ff9800", fg="white", 
                           command=lambda: perform_operation("divide"))
divide_button.grid(row=1, column=1, padx=10, pady=10)


result_label = tk.Label(root, text="Result: ", font=("Arial", 14), bg="#e3f2fd", fg="#333")
result_label.pack(pady=20)

root.mainloop()
