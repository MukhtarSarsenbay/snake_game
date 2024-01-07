from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24 , "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #turtle to keep track a score
        #display on the program
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game is over!", move=False, align=ALIGNMENT, font=FONT)

    def count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
