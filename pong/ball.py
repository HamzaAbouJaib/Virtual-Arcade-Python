from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):

        super().__init__("circle")
        self.color("white")
        self.penup()


        self.x_move = 10
        self.y_move = 10


    def move(self):
        """
        The function move() takes the current x and y coordinates of the ball and adds the x and y
        movement values to them. 
        
        The new coordinates are then passed to the goto() function, which moves the ball to the new
        coordinates
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)


    def bounce_y(self):
        """
        If the ball hits the top or bottom of the screen, it will bounce off
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        If the ball hits the left or right paddle, it will bounce off and move in the
        opposite direction
        """
        self.x_move *= -1


    def reset(self):
        """
        The function resets the position of the ball to the center of the screen
        """
        self.home()
        self.bounce_x()