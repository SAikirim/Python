from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10, 25,25, fill=color)  # 공
        self.canvas.move(self.id, 230, 270)
        self.score_id = canvas.create_text(450, 10, text='score %d' % score)    # 점수판

        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.started = False
        self.canvas.bind_all('<Button-1>', self.start_ball) # 시작
        self.acceleration = 0
        self.score = 0


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score += 1
                canvas.itemconfig(self.score_id, text='score %d' % self.score)  # 점수 기록
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.acceleration = (self.score % 5) *0.2     # 점수로 난이도 상승

        if pos[0] <= 0:
            self.x = 3 + self.acceleration
        if pos[2] >= self.canvas_width:
            self.x = -3 - self.acceleration
        if pos[1] <= 0:
            self.y = 3 + self.acceleration
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3 - self.acceleration


    def start_ball(self,evt):
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.started = True



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,evt):
        self.x = -3
    def turn_right(self,evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

score = 0
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, 'red')
game_over = canvas.create_text(250,150, text='GAME OVER', state='hidden')


while 1:
    if ball.hit_bottom == False and ball.started == True:
        paddle.draw()
        ball.draw()
    elif ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over, state='normal')


    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)