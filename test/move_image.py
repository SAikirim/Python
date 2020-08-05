from tkinter import *
from PIL import Image
import time

# png파일 gif로 변환
img = Image.open("/root/sys.png")
size = (200, 200)
print(img.size)
img.thumbnail(size)
img.save("/root/sys.gif")

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
my_image = PhotoImage(file='/root/sys.gif')
mytriangle = canvas.create_image(0,0, anchor=NW, image=my_image)

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