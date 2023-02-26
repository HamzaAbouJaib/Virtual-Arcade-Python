from turtle import Screen
from snake.snake import Snake

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