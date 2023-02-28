from turtle import Turtle

class Scoreboard(Turtle):

    # Constant properties
    ALIGNMENT = "center"
    FONT = ("Courier", 80, "normal")

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0

        self.update()


    def update(self):
        """
        Writes the left and right scores to the screen
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=self.ALIGNMENT, font=self.FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=self.ALIGNMENT, font=self.FONT)


    def left_point(self):
        """
        Adds 1 to the left_score variable and then calls the update() function
        """
        self.left_score += 1
        self.update()


    def right_point(self):
        """
        Adds 1 to the right_score variable and then calls the update() function
        """
        self.right_score += 1
        self.update()