from turtle import Turtle

class Pedal(Turtle):
    def __init__(self, x, screen):
        super().__init__()
        self.screen = screen
        self.x = x
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, 0)
        self.move_speed = 20
        self.moving_up = False
        self.moving_down = False

    def go_up(self):
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            if new_y < self.screen.window_height() // 2 - 50:  # Boundary check
                self.goto(self.x, new_y)
            self.screen.ontimer(self.go_up, 100)  # Adjust the timer delay for speed

    def go_down(self):
        if self.moving_down:
            new_y = self.ycor() - self.move_speed
            if new_y > -self.screen.window_height() // 2 + 50:  # Boundary check
                self.goto(self.x, new_y)
            self.screen.ontimer(self.go_down, 100)  # Adjust the timer delay for speed

    def start_moving_up(self):
        self.moving_up = True
        self.go_up()

    def stop_moving_up(self):
        self.moving_up = False

    def start_moving_down(self):
        self.moving_down = True
        self.go_down()

    def stop_moving_down(self):
        self.moving_down = False
