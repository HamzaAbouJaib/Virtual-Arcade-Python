from turtle import Screen
from snake.snake import Snake

class SnakeGame():

    def __init__(self):
        self.snake = Snake()
        self.screen = Screen()
        self.screen.title("Snake Game")

    def run_game(self):
        pass