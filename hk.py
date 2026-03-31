import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Мой Paint")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

color = "black"
size = 3
drawing = False

canvas = tk.Canvas(root, bg="white", width=800, height=500, bd=2, relief=tk.GROOVE)
canvas.pack(pady=10)

def start_draw(event):
    global drawing, last_x, last_y
    drawing = True
    last_x = event.x
    last_y = event.y

def draw(event):
    global drawing, last_x, last_y
    if drawing:
        x, y = event.x, event.y
        canvas.create_line(last_x, last_y, x, y, fill=color, width=size, capstyle=tk.ROUND, smooth=True)
        last_x, last_y = x, y

def stop_draw(event):
    global drawing
    drawing = False

def change_color():
    global color
    color_code = colorchooser.askcolor(title="Выбери цвет")
    if color_code:
        color = color_code[1]

def set_red():
    global color
    color = "red"

def set_blue():
    global color
    color = "blue"

def set_green():
    global color
    color = "green"

def set_black():
    global color
    color = "black"

def set_yellow():
    global color
    color = "yellow"

def set_purple():
    global color
    color = "purple"

def set_orange():
    global color
    color = "orange"

def use_eraser():
    global color
    color = "white"

def bigger():
    global size
    size += 1
    size_label.config(text=f"Размер: {size}")

def smaller():
    global size
    if size > 1:
        size -= 1
    size_label.config(text=f"Размер: {size}")

def clear_all():
    canvas.delete("all")

def create_styled_button(parent, text, bg_color, fg_color, command):
    btn = tk.Button(parent, text=text, bg=bg_color, fg=fg_color, command=command,
                    font=("Arial", 10, "bold"), padx=15, pady=5,
                    relief=tk.RAISED, bd=2, cursor="hand2")
    btn.bind("<Enter>", lambda e: btn.config(bg=lighten_color(bg_color), relief=tk.SUNKEN))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg_color, relief=tk.RAISED))
    return btn

def lighten_color(color):
    colors = {
        "black": "#333333",
        "red": "#ff6666",
        "blue": "#6666ff",
        "green": "#66ff66",
        "yellow": "#ffff66",
        "purple": "#cc66ff",
        "orange": "#ffcc66",
        "white": "#e0e0e0"
    }
    return colors.get(color, color)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

panel = tk.Frame(root, bg="#f0f0f0")
panel.pack(pady=5)

btn_black = create_styled_button(panel, "Черный", "black", "white", set_black)
btn_black.grid(row=0, column=0, padx=3, pady=3)

btn_red = create_styled_button(panel, "Красный", "red", "white", set_red)
btn_red.grid(row=0, column=1, padx=3, pady=3)

btn_blue = create_styled_button(panel, "Синий", "blue", "white", set_blue)
btn_blue.grid(row=0, column=2, padx=3, pady=3)

btn_green = create_styled_button(panel, "Зеленый", "green", "white", set_green)
btn_green.grid(row=0, column=3, padx=3, pady=3)

btn_yellow = create_styled_button(panel, "Желтый", "yellow", "black", set_yellow)
btn_yellow.grid(row=0, column=4, padx=3, pady=3)

btn_purple = create_styled_button(panel, "Фиолетовый", "purple", "white", set_purple)
btn_purple.grid(row=0, column=5, padx=3, pady=3)

btn_orange = create_styled_button(panel, "Оранжевый", "orange", "black", set_orange)
btn_orange.grid(row=0, column=6, padx=3, pady=3)

btn_eraser = create_styled_button(panel, "🧽 Ластик", "white", "black", use_eraser)
btn_eraser.grid(row=0, column=7, padx=3, pady=3)

btn_plus = create_styled_button(panel, "+", "#4CAF50", "white", bigger)
btn_plus.grid(row=0, column=8, padx=3, pady=3)

btn_minus = create_styled_button(panel, "-", "#f44336", "white", smaller)
btn_minus.grid(row=0, column=9, padx=3, pady=3)

btn_clear = create_styled_button(panel, "🗑 Очистить", "#FF9800", "white", clear_all)
btn_clear.grid(row=0, column=10, padx=3, pady=3)

btn_color = create_styled_button(panel, "🎨 Выбрать цвет", "#9C27B0", "white", change_color)
btn_color.grid(row=0, column=11, padx=3, pady=3)

size_label = tk.Label(panel, text=f"Размер: {size}", bg="#f0f0f0", font=("Arial", 10, "bold"))
size_label.grid(row=0, column=12, padx=10)

root.mainloop()