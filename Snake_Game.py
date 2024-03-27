import turtle
import random
import time
from turtle import *

delay = 1
snake = []
score = 0
high_score = 0

# Creating the head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.shapesize(0.50, 0.50)
head.goto(0, 50)
head.direction = "stop"

# Creating the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 330)
score_display.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

# Functions for directions
def up():
    if head.direction != "down":
        head.direction = "up"
 
def down():
    if head.direction != "up":
        head.direction = "down"
 
def right():
    if head.direction != "left":
        head.direction = "right"
 
def left():
    if head.direction != "right":
        head.direction = "left"

def restart():
    global score
    score = 0
    update_score()          # update the score after game over/ restart, i.e, initializing score again to 0
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)         # update the position of food after game over/ restart
    clear()
    move()

# Game over after collision
def game_over():
    global high_score
    if score > high_score:
        high_score = score
    update_score()          # Update the high_score after game over
    clear()
    head.goto(0, 0)
    write("Game Over. Press 'R' to restart.", align="center", font=("Courier", 24, "normal"))
    onkey(restart, 'r')     # Assigning key to restart the function

# Update the score
def update_score():
    score_display.clear()
    score_display.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

# Close the game 
def close_game():
    bye()                   # Shutting down the game window 

# Define the boundaries of the game area
left_bound = -290
right_bound = 290
top_bound = 290
bottom_bound = -290
border_width = 3

# Define the border of the playing area
def draw_border():
    "Draw borders of the game area"
    border_pen = Turtle()
    border_pen.speed(0)
    border_pen.color("black")
    border_pen.width(border_width)
    border_pen.penup()
    border_pen.goto(left_bound, top_bound)
    border_pen.pendown()
    border_pen.goto(right_bound, top_bound)
    border_pen.goto(right_bound, bottom_bound)
    border_pen.goto(left_bound, bottom_bound)
    border_pen.goto(left_bound, top_bound)
    border_pen.hideturtle()

# Define the function to move the snake
def move():
    "Move snake forward one segment."
    global score

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)   # y coordinate of the snake
    
    if head.direction == "down":
        y = head.ycor()     # y coordinate of the snake
        head.sety(y - 15)
 
    if head.direction == "right":
        x = head.xcor()     # y coordinate of the snake
        head.setx(x + 15)
 
    if head.direction == "left":
        x = head.xcor()     # y coordinate of the snake
        head.setx(x - 15)
    
    if head.distance(food) < 15:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x, y)     # Changing the position of food after head catches the food

        score += 1          # Incrementing score each time head cathches the food
        score_display.clear()
        score_display.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        new_segment.shapesize(0.50, 0.50)
        snake.append(new_segment)       # Incrementing the length of the snake each time head catches the food

    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)             # Assigning positions to the new_segment to move with the head

    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x, y)             # Assigning position to the 0th segment to move with the head
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:          # Checking for the collision of head with the boudaries 
        update()
        game_over()                     
        for i in snake:
            i.goto(1000, 1000)              # Hide the new segments added before the next game
        snake.clear()
        return

    for i in snake[1:]:         # Checking for the collision of head with the body
        if i.distance(head) < 5:
            update()
            game_over()
            for i in snake:
                i.goto(1000, 1000)          # Hide the new segments added before the next game
            snake.clear()
            return                
        
    clear()
    update()
    ontimer(move, 100)          # Call move function again after delay(100)

# Creating the screen
Screen()
title("Snakes Game")
bgcolor("#87CEFA")
setup(width = 700, height = 800)
hideturtle()
tracer(False)

# Keybindings for movement of snake
listen()
onkey(right, 'D')
onkey(right, 'Right')
onkey(right, 'd')

onkey(left, 'A')
onkey(left, 'Left')
onkey(left, 'a')

onkey(up, 'W')
onkey(up, 'Up')
onkey(up, 'w')

onkey(down, 'S')
onkey(down, 'Down')
onkey(down, 's')

# to close or quit the game window
onkey(close_game, 'q')   

draw_border()  # draw border for the game area
move()         # Start the game  
time.sleep(delay)
done()