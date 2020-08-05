from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
#mytriangle = canvas.create_polygon(10,10, 10,60, 50,35)

def random_triangle(x, y, color):
    x1 = random.randrange(x)
    y1 = random.randrange(y)
    x2 = x1 + random.randrange(x)
    y2 = random.randrange(y)
    x3 = random.randrange(x)
    y3 = y1 + random.randrange(y)
    canvas.create_polygon(x1,y1, x2,y2, x3,y3, fill=color, outline='black')

for x in range(100):
    color = ['#'+"".join([random.choice('1234567890ABCDF') for x in range(6)])]
    random_triangle(400, 400, color)