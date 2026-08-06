import tkinter as tk

def greet():
    message.config(text="Hello from my first GUI!")
    
window = tk.Tk()
window.title("Simple GUI")
window.geometry("620x220")
message = tk.Label(window,text = "Click the button",font =("Arial",18))

message.pack(pady=40)
button = tk.Button(window,text="Greet me",command=greet)
button.pack()
window.mainloop()