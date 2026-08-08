import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / height ** 2
        result.config(text=f"BMI: {bmi:.2f}")
    except (ValueError,ZeroDivisionError):
        messagebox.showerror("Input","Enter valid metric values.")

window = tk.Tk(); window.title("BMI Calculator")
tk.Label(window,text="Weight in kg").pack()
weight_entry = tk.Entry(window); weight_entry.pack()
tk.Label(window,text="Height in meters").pack()
height_entry = tk.Entry(window); height_entry.pack()
tk.Button(window,text="Calculate",command=calculate).pack(pady=10)
result = tk.Label(window,text="BMI: --",font=("Arial",18)); result.pack()
window.mainloop()


        