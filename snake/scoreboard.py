from turtle import Turtle

class Scoreboard(Turtle):

    # Constant properties
    ALIGNMENT = "center"
    FONT = ("Arial", 20, "normal")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.score = 0


    def display(self):
        """
        It displays the score on the screen
        """
        self.write(f"Score: {self.score}", align=self.ALIGNMENT, font=self.FONT)

    
    def update(self):
        """
        The function update() is called every time the game loop runs. It clears the screen, updates the
        score, and displays the score
        """
        self.score += 1
        self.clear()
        self.display()


    def game_over(self):
        self.home()
        self.write(f"Game Over!", align=self.ALIGNMENT, font=self.FONT)
        self.goto(0, -30)
        self.write(f"Click Anywhere to Exit", align=self.ALIGNMENT, font=self.FONT)