import tkinter as tk
from tkinter import colorchooser

def choose_color():
    global pen_color
    color_code = colorchooser.askcolor(title="Выбери цвет")
    if color_code[1]:
        pen_color = color_code[1]

drawing = False
last_x, last_y = None, None
pen_color = "black"

def start_drawing(event):
   global drawing, last_x, last_y
   drawing = True
   last_x, last_y = event.x, event.y
def stop_drawing(event):
    global drawing
    drawing = False
def draw(event):
    global last_x, last_y
    if drawing:
        x, y = event.x, event.y
        canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=2, capstyle=tk.ROUND, smooth = True)
        last_x, last_y = x, y
def change_color(new_color):
    global pen_color
    pen_color = new_color

root = tk.Tk()
root.title("my paint")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<ButtonRelease-1>", stop_drawing)
canvas.bind("<B1-Motion>", draw)

tools_frame = tk.Frame(root)
tools_frame.pack()

colors = ["red", "green", "blue", "black", "orange", "pink"]
for color in colors:
    btn = tk.Button(tools_frame, text=color.capitalize(), bg=color,
                    command=lambda c=color: change_color(c))
    btn.pack(side=tk.LEFT, padx=2)

root.mainloop()