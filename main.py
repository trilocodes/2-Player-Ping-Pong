# ------------------------TODO start the game on pressing spacebar--------------------------
from turtle import Screen,bgpic
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
l_paddle = Paddle((-800,0))
r_paddle = Paddle((+800,0))
ball = Ball()
scoreboard = Scoreboard()
bgpic("bg.gif") 
# screen.setup(width=800, height=600)
# screen.bgcolor("#03002b")
# screen.bgcolor("#7C0202")
screen.title("Ping Pong")
screen.tracer(0)

# -----------------------------  This makes it fullscreen   -------------------------------
# ------------------  Assumed Dimensions of fullscreen = 1600 X 1040   --------------------
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
#------------------------------------------------------------------------------------------

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection with wall
    if ball.ycor()>=520 or ball.ycor()<=-510:
        ball.wall_bounce()
    if ball.xcor()>=835 or ball.xcor()<=-839:
        ball.reset_position()

    # Detection with paddle
    if ball.distance(r_paddle)<=102 and ball.xcor()>=785:
        ball.paddle_bounce()
        ball.move_speed*=0.6
    if ball.distance(l_paddle)<=102 and ball.xcor()<=-785:
        ball.paddle_bounce()
        ball.move_speed*=0.6
    
    # Right paddle misses
    if ball.xcor()>=810:
        ball.reset_speed()
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses
    if ball.xcor()<=-815:
        ball.reset_speed()
        ball.reset_position()
        scoreboard.r_point()
    
    # Checking for the winner
    if scoreboard.l_score == 5:
        scoreboard.declare_winner(1)
        game_is_on = False
    if scoreboard.r_score == 5:
        scoreboard.declare_winner(2)
        game_is_on = False
    
screen.exitonclick()