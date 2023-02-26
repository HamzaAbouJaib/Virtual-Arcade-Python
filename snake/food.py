from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, shape="circle"):
        super().__init__(shape=shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(50)
        self.refresh()


    def refresh(self):
        """
        It refreshes the food's position to a random location on the screen.
        """
        self.goto(x=randint(-580, 580), y=randint(-580, 580))