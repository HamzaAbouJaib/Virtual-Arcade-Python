from turtle import Turtle

class Snake():

    def __init__(self):
        self.segments = []
        # The postitions of the initial three segments of a snake
        self.positions = [(0, 0), (-20, 0), (-40, 0)]

        # Create the initial three segments that make up the snake
        for position in self.positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)


        

    