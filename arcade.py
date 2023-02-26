from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

game_choice = screen.textinput(title="Select a game", prompt="Which game would you like to play? (snake/pong): ")

if game_choice.lower() == "snake":
    screen.title("Snake Game")

elif game_choice.lower() == "pong":
    screen.title("Pong Game")
    screen.setup(width=800, height=600)

screen.exitonclick()