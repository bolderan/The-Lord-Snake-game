import turtle as T
import random
import time
import day20_2
from day20_4 import Scoreboard
from day20_3 import Food
screen = T.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Project NAGRAJ")
screen.tracer(0)
  
snake = day20_2.Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right ")

game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move() 
    # colision detection with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increse_score()
    # detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_()
        snake.reset_()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset_()
            snake.reset_()


screen.exitonclick()
