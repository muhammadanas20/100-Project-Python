import tkinter as tk

count = 0

def add_click():
    global count
    count += 1
    label.config(text=str(count))


def reset():
    global count
    count = 0
    label.config(text="0")

window = tk.Tk()
label = tk.Label(window,text="0",font=("Arial",50))
label.pack(padx=100,pady=40)

tk.Button(window,text="Click",command=add_click).pack()
tk.Button(window,text="Reset",command=reset).pack(pady = 8) 
window.mainloop()