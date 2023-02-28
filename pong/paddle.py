from turtle import Turtle

class Paddle(Turtle):

    MOVE_DISTANCE = 20

    def __init__(self, xcor, ycor):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5)
        self.goto(x=xcor, y=ycor)
        self.setheading(90)


    def move_up(self):
        """
        If the turtle's y coordinate is less than the canvas width minus 50, then move the turtle
        up the screen by the MOVE_DISTANCE
        """
        if self.ycor() < 250:
            self.forward(self.MOVE_DISTANCE)


    def move_down(self):
        """
        If the turtle's y coordinate is greater than the negative width of the screen plus 50, then move
        the turtle down the screen by the MOVE_DISTANCE
        """
        if self.ycor() > -250:
            self.backward(self.MOVE_DISTANCE)
