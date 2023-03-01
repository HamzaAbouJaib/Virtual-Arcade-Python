from turtle import Turtle

class Scoreboard(Turtle):

    # Constant properties
    ALIGNMENT = "center"
    FONT = ("Courier", 80, "normal")
    GAME_OVER_FONT = ("Courier", 20, "normal")

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

    
    def get_winner(self):

        if self.right_score > self.left_score:
            return "Player 1"
        else: 
            return "Player 2"


    def game_over(self):
        """
        Prints out the winner of the game, and then prints out "Click Anywhere to Exit"
        """
        self.goto(0, 30)
        self.write(f"Game Over!", align=self.ALIGNMENT, font=self.GAME_OVER_FONT)
        self.goto(0, 0)
        self.write(f"{self.get_winner()} Won!", align=self.ALIGNMENT, font=self.GAME_OVER_FONT)
        self.goto(0, -30)
        self.write(f"Click Anywhere to Exit", align=self.ALIGNMENT, font=self.GAME_OVER_FONT)