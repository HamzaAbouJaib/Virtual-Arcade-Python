from turtle import Turtle

class Scoreboard(Turtle):

    # Constant properties
    ALLIGNMENT = "center"
    FONT = ("Arial", 20, "normal")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.score = 0


    def display_score(self):
        """
        It displays the score on the screen
        """
        self.write(f"Score: {self.score}", align=self.ALLIGNMENT, font=self.FONT)