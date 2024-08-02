from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0,0)
        self.dx=10
        self.dy=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.dx
        new_y=self.ycor()+self.dy
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.dy*=-1

    def bounce_x(self):
        self.dx*=-1
        self.move_speed*=0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()








