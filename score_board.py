from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.s1 = 0
        self.s2 = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.write_score()



    def write_score(self):
        self.goto(-100, 200)
        self.write(self.s1, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.s2, align='center', font=('Courier', 80, 'normal'))





