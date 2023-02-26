from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)

game_choice = screen.textinput(title="Select a game", prompt="Which game would you like to play? (snake/pong): ")

screen.exitonclick()