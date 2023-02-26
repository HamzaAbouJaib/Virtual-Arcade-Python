from turtle import Turtle

class Snake():


    RIGHT = 0
    LEFT = 180
    UP = 90
    DOWN = 270

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
        Adds a new segment to the snake's body, positioned at the end of the snake's body
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
        """
        If the snake's head is not facing down, then set the snake's head to face up
        """
        if (self.head.heading() != self.DOWN):
            self.head.setheading(self.UP)

    def move_down(self):
        """
        If the snake's head is not facing up, then set the snake's head to face down
        """
        if (self.head.heading() != self.UP):
            self.head.setheading(self.DOWN)

    def move_left(self):
        """
        If the snake is not moving right, then it will move left
        """
        if (self.head.heading() != self.RIGHT):
            self.head.setheading(self.LEFT)

    def move_right(self):
        """
        If the snake is not moving left, then set the snake's heading to right
        """
        if (self.head.heading() != self.LEFT):
            self.head.setheading(self.RIGHT)

    