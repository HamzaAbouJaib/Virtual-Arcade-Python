from turtle import Turtle

class Food(Turtle):

    def __init__(self, shape="circle"):
        super().__init__(shape=shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(50)