import tkinter as tk
from tkinter.colorchooser import askcolor

def change_color(shape_id):
    # Open color chooser and get the selected color
    color = askcolor()[1]
    if color:
        canvas.itemconfig(shape_id, fill=color)

def create_circle(x, y, r, **kwargs):
    # Helper function to create a circle
    return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

def create_rectangle(x, y, width, height, **kwargs):
    # Helper function to create a rectangle
    return canvas.create_rectangle(x, y, x + width, y + height, **kwargs)

# Initialize the main window
root = tk.Tk()
root.title("Interactive Color Palette")

# Create a canvas to draw shapes
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Draw some shapes on the canvas
circle = create_circle(150, 150, 50, fill="red", outline="black")
rectangle = create_rectangle(250, 100, 100, 80, fill="blue", outline="black")
triangle = canvas.create_polygon(300, 300, 350, 250, 400, 300, fill="green", outline="black")

# Add buttons to change colors of shapes
circle_button = tk.Button(root, text="Change Circle Color", command=lambda: change_color(circle))
circle_button.pack(pady=5)

rectangle_button = tk.Button(root, text="Change Rectangle Color", command=lambda: change_color(rectangle))
rectangle_button.pack(pady=5)

triangle_button = tk.Button(root, text="Change Triangle Color", command=lambda: change_color(triangle))
triangle_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

