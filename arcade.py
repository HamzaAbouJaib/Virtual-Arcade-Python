from turtle import Screen
from snake.snake_game import SnakeGame
from pong.pong_game import PongGame

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_choice = screen.textinput(title="Select a game", prompt="Which game would you like to play? (snake/pong): ")

if game_choice.lower() == "snake":
    snake_game = SnakeGame()
    snake_game.run_game()

elif game_choice.lower() == "pong":
    pong_game = PongGame()
    pong_game.run_game()

screen.exitonclick()