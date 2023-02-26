from turtle import Turtle

class Snake():

    def __init__(self):
        self.segments = []
        # The postitions of the initial three segments of a snake
        self.positions = [(0, 0), (-20, 0), (-40, 0)]

        # Create the initial three segments that make up the snake
        for position in self.positions:
            self.add_segment(position)

        # The head of the snake
        self.head = self.segments[0]


    def add_segment(self, position):
        """
        The function add_segment() takes in a position and creates a new segment at that position
        
        :param position: The position of the new segment
        """
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    
    def extend_snake(self):
        """
        It adds a new segment to the snake's body, positioned at the end of the snake's body
        """
        self.add_segment(self.segments[-1].position())


    def move(self):
        """
        The function moves the snake by moving each segment to the position of the segment in front of
        it, and then moves the head in the direction of the snake
        """
        for i in range(len(self.segments)-1, 0, -1):
            front_segment = self.segments[i-1]
            self.segments[i].goto(front_segment.xcor(), front_segment.ycor()) 
        self.head.forward(20)   


    def move_up(self):
        if (self.head.heading() != 270):
            self.head.setheading(90)

    def move_down(self):
        if (self.head.heading() != 90):
            self.head.setheading(270)

    def move_left(self):
        if (self.head.heading() != 0):
            self.head.setheading(180)

    def move_right(self):
        if (self.head.heading() != 180):
            self.head.setheading(0)

    