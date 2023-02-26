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

            # Detect collisions with the wall/boarder
            game_on = not self.wall_collision()

            # Detect collisions with self
            game_on = not self.self_collision()



    def wall_collision(self):
        """
        If the snake's head is outside of the screen, return True
        :return: The x and y coordinates of the snake's head.
        """
        return self.snake.head.xcor() > 580 or self.snake.head.xcor() < -580 or self.snake.head.ycor() > 580 or self.snake.head.ycor() < -580
    

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