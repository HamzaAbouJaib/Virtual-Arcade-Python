from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):

        super().__init__("circle")
        self.color("white")
        self.penup()


    