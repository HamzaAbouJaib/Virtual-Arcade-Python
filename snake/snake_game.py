from turtle import Screen
from snake.snake import Snake
from snake.food import Food
from snake.scoreboard import Scoreboard
from time import sleep

class SnakeGame():

    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen = Screen()
        self.screen.title("Snake Game")

    def run_game(self):
        self.screen.listen()
        self.screen.onkey(self.snake.move_up, "w")
        self.screen.onkey(self.snake.move_down, "s")
        self.screen.onkey(self.snake.move_left, "a")
        self.screen.onkey(self.snake.move_right, "d")

        self.scoreboard.display()
        
        while True:
            self.screen.update()
            # Slow down the update speed
            sleep(0.1)
            self.snake.move()

            # Detech collision with food
            self.food_collision()

            # Detect collisions with the wall/boarder
            if self.wall_collision():
                break

            # Detect collisions with self
            if self.self_collision():
                break


    def food_collision(self):
        """
        If the distance between the snake's head and the food is less than 15, refresh the food and
        extend the snake
        """
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.extend_snake()
            self.scoreboard.update()


    def wall_collision(self):
        """
        If the snake's head is outside of the screen, return True
        :return: The x and y coordinates of the snake's head.
        """
        return self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280
    

    def self_collision(self):
        """
        If the distance between the head and any other segment is less than 10 it means the segments likely touched, return True. Otherwise,
        return False
        :return: The distance between the head and the segment.
        """
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                return True
        return False