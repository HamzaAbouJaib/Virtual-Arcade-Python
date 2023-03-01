from turtle import Screen, Turtle
from pong.paddle import Paddle
from pong.ball import Ball
from pong.scoreboard import Scoreboard
from time import sleep


class PongGame():

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Pong Game")
        self.screen.setup(width=800, height=600)

        self.right_paddle = Paddle(350, 0)
        self.left_paddle = Paddle(-350, 0)
        self.ball = Ball()
        self.scoreboard = Scoreboard()


    def instructions(self):
        instruction_writer = Turtle()
        instruction_writer.penup()
        instruction_writer.hideturtle()
        instruction_writer.color("white")
        instruction_writer.goto(0, 30)
        instruction_writer.write("Player1: Use Up and Down arrows to move the paddle", align="center", font=("Arial", 20, "normal"))
        instruction_writer.goto(0, 0)
        instruction_writer.write("Player2: Use W and S keys to move the paddle", align="center", font=("Arial", 20, "normal"))
        instruction_writer.goto(0, -30)
        instruction_writer.write("Game will start in 5 seconds", align="center", font=("Arial", 20, "normal"))

        sleep(5)

        instruction_writer.clear()
        instruction_writer.reset()



    def run_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.right_paddle.move_up, "Up")
        self.screen.onkeypress(self.right_paddle.move_down, "Down")
        self.screen.onkeypress(self.left_paddle.move_up, "w")
        self.screen.onkeypress(self.left_paddle.move_down, "s")

        self.instructions()

        while True:
            self.screen.update()
            sleep(self.ball.move_speed)

            self.ball.move()

            if self.ball.xcor() < 390 and self.ball.xcor() > -390:
                if self.ball.xcor() < 360 and self.ball.xcor() > -360:
                    # If the ball touches the upper or lower side of the screen, then bounce the ball
                    if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                        self.ball.bounce_y()
                    # If the ball touches the left or right paddle, then bounce the ball
                    if self.ball.distance(self.right_paddle) < 50 and self.ball.xcor() > 330 or self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() < -330:
                        self.ball.bounce_x()


            else:
                if self.ball.xcor() > 360:
                    self.scoreboard.left_point()
                elif self.ball.xcor() < -360:
                    self.scoreboard.right_point()
                self.ball.reset()


