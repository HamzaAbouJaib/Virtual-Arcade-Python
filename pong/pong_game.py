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


        while True:
            self.screen.update()
            sleep(0.1)


