from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.shapesize(stretch_len=1.1, stretch_wid=1.1)
        self.penup()
        self.goto(0,0)
        self.x_move = 1
        self.y_move = 1
        self.reset_speed()

    def move(self):
        x = self.xcor()+ self.x_move
        y = self.ycor()+ self.y_move
        self.goto(x,y)
    
    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
    
    def reset_speed(self):
        self.move_speed = 0.0005