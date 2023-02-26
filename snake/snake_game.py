from turtle import Screen
from snake.snake import Snake
from time import sleep

class SnakeGame():

    def __init__(self):
        self.snake = Snake()
        self.screen = Screen()
        self.screen.title("Snake Game")

    def run_game(self):
        self.screen.listen()
        self.screen.onkey(self.snake.move_up, "w")
        self.screen.onkey(self.snake.move_down, "s")
        self.screen.onkey(self.snake.move_left, "a")
        self.screen.onkey(self.snake.move_right, "d")


        game_on = True

        while game_on:
            self.screen.update()
            # Slow down the update speed
            sleep(0.1)
            self.snake.move()