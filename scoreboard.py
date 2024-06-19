from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-200,430)
        self.write(self.l_score, align="center", font=("Impact", 60, "normal"))
        self.goto(200,430)
        self.write(self.r_score, align="center", font=("Impact", 60, "normal"))
        
    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()
    
    def declare_winner(self, a):
        self.goto(5,-50)
        if a==1: 
            self.write("✨ PLAYER 1 WINS ✨", align="center", font=("Impact", 70, "normal"))
        if a==2: 
            self.write("✨ PLAYER 2 WINS ✨", align="center", font=("Impact", 70, "normal"))
