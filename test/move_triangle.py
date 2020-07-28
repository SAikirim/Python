from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10,10, 10,60, 50,35)

def move_triangle(x, y):
    canvas.move(mytriangle, x, y)
    tk.update()
    time.sleep(0.04)

for x in range(60):
    move_triangle(5, 5)

for x in range(60):
    move_triangle(-5, 0)

for x in range(60):
    move_triangle(0, -5)