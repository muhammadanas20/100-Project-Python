import tkinter as tk

# Initialize global variables for tracking coordinates
last_x = last_y = None

def start(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    # Draw a line from the last recorded point to the current mouse position
    canvas.create_line(last_x, last_y, event.x, event.y, width=4, fill="black")
    last_x, last_y = event.x, event.y

# Set up main window
window = tk.Tk()
window.title("Drawing Pad")

# Configure canvas
canvas = tk.Canvas(window, width=600, height=400, bg="blue")
canvas.pack()

# Bind mouse events to the canvas
canvas.bind("<Button-1>", start)
canvas.bind("<B1-Motion>", draw)

# Button to clear the canvas
tk.Button(window, text="Clear", command=lambda: canvas.delete("all")).pack()

window.mainloop()
