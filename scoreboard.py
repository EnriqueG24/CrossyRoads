from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 0
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
