from turtle import Screen
from pedal import Pedal
from ball import Ball
from score_board import ScoreBoard
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.tracer(0)

l_pedal = Pedal(-350, screen)  # Left paddle
r_pedal = Pedal(350, screen)   # Right paddle
ball = Ball()
score = ScoreBoard()
line=Line()

screen.listen()
screen.onkeypress(l_pedal.start_moving_up, 'w')
screen.onkeyrelease(l_pedal.stop_moving_up, 'w')
screen.onkeypress(l_pedal.start_moving_down, 's')
screen.onkeyrelease(l_pedal.stop_moving_down, 's')

screen.onkeypress(r_pedal.start_moving_up, 'Up')
screen.onkeyrelease(r_pedal.stop_moving_up, 'Up')
screen.onkeypress(r_pedal.start_moving_down, 'Down')
screen.onkeyrelease(r_pedal.stop_moving_down, 'Down')


game_on = True
while game_on:
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with the top and bottom walls
    if abs(ball.ycor()) > 285:
        ball.bounce_y()

    # Detect collision with the paddles
    if (ball.xcor() > 320 and ball.distance(r_pedal) < 50) or (ball.xcor() < -320 and ball.distance(l_pedal) < 50):
        ball.bounce_x()


    # Detect Missed
    if ball.xcor() > 380:
        ball.reset()
        score.clear()
        score.s2+=1
        score.write_score()



    if ball.xcor() < -380:
        ball.reset()
        score.clear()
        score.s1+=1
        score.write_score()



    screen.update()

screen.exitonclick()
