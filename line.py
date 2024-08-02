from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.goto(0, -300)
        self.draw()

    def draw(self):
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)