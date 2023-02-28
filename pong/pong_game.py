from turtle import Screen
from pong.paddle import Paddle
from pong.ball import Ball
from time import sleep


class PongGame():

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Pong Game")
        self.screen.setup(width=800, height=600)

        self.right_paddle = Paddle(350, 0)
        self.left_paddle = Paddle(-350, 0)
        self.ball = Ball()


    def run_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.right_paddle.move_up, "Up")
        self.screen.onkeypress(self.right_paddle.move_down, "Down")
        self.screen.onkeypress(self.left_paddle.move_up, "w")
        self.screen.onkeypress(self.left_paddle.move_down, "s")


        sleep(0.4)

        while True:
            self.screen.update()
            sleep(0.1)

            self.ball.move()

            if self.ball.xcor() < 390 and self.ball.xcor() > -390:
                if self.ball.xcor() < 360 and self.ball.xcor() > -360:
                    # If the ball touches the upper or lower side of the screen, then bounce the ball
                    if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                        self.ball.bounce_y()
                    # If the ball touches the left or right paddle, then bounce the ball
                    if self.ball.distance(self.right_paddle) < 50 and self.ball.xcor() > 330 or self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() < -330:
                        self.ball.bounce_x()


