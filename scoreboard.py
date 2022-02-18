from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
SIDE = {"left": (-200, 270), "right": (200, 270)}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(SIDE["left"])
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(SIDE["right"])
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def update_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def update_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write("Game Over. The Left Player has won!", align=ALIGNMENT, font=FONT)
        else:
            self.write("Game Over. The Right Player has won!", align=ALIGNMENT, font=FONT)
