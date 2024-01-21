from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=280)
        self.rewrite_score()

    def rewrite_score(self):
        self.goto(x=0, y=280)
        self.clear()
        self.write(f"Score: {self.user_score}", True, align=ALIGNMENT, font=FONT)

    def print_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", True, align=ALIGNMENT, font=FONT)

    def update(self):
        self.user_score += 1
        self.rewrite_score()
