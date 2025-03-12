import tkinter as tk
from tkinter import messagebox

def on_operation_click(operation):
    try:
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_label.config(text=f"Result: {num1} {operation} {num2} = {result}", fg='green')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear_fields():
    input_num1.delete(0, tk.END)
    input_num2.delete(0, tk.END)
    result_label.config(text="Result: ", fg='black')

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.configure(bg='#4DCCF3')

label_num1 = tk.Label(root, text="Enter first number:", bg='#f0f0f0', font=('Arial', 12))
label_num1.grid(row=0, column=0, padx=10, pady=10)

input_num1 = tk.Entry(root, font=('Arial', 12))
input_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:", bg='#f0f0f0', font=('Arial', 12))
label_num2.grid(row=1, column=0, padx=10, pady=10)

input_num2 = tk.Entry(root, font=('Arial', 12))
input_num2.grid(row=1, column=1, padx=10, pady=10)

operations_frame = tk.Frame(root, bg='#4DCCF3')
operations_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

button_add = tk.Button(operations_frame, text="+", command=lambda: on_operation_click('+'), bg='#4CAF50', fg='white', font=('Arial', 12), width=5)
button_add.grid(row=0, column=0, padx=5, pady=5)

button_subtract = tk.Button(operations_frame, text="-", command=lambda: on_operation_click('-'), bg='#f44336', fg='white', font=('Arial', 12), width=5)
button_subtract.grid(row=0, column=1, padx=5, pady=5)

button_multiply = tk.Button(operations_frame, text="*", command=lambda: on_operation_click('*'), bg='#2196F3', fg='white', font=('Arial', 12), width=5)
button_multiply.grid(row=0, column=2, padx=5, pady=5)

button_divide = tk.Button(operations_frame, text="/", command=lambda: on_operation_click('/'), bg='#FF9800', fg='white', font=('Arial', 12), width=5)
button_divide.grid(row=0, column=3, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields, bg='#9E9E9E', fg='white', font=('Arial', 12))
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", bg='#f0f0f0', font=('Arial', 14))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()