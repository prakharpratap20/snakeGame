# import turtle graphics module
import turtle
import random

# defining program constants
WIDTH = 600
HEIGHT = 600
DELAY = 100 # milliseconds
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    
def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if direction != "down": # To avoid self collision simply by pressing the wrong key
            snake_direction = "up"
    elif direction == "down":
        if direction != "up": # To avoid self collision simply by pressing the wrong key
            snake_direction = "down"
    elif direction == "right":
        if direction != "left": # To avoid self collision simply by pressing the wrong key
            snake_direction = "right"
    elif direction == "left":
        if direction != "right": # To avoid self collision simply by pressing the wrong key
            snake_direction = "left"

def game_loop():
    stamper.clearstamps() # remove existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
    
    #check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        
    
        # add new head to snake body
        snake.append(new_head)
        
        # check food collision
        if not food_collision():
            snake.pop(0) # keep the snake same length unless fed.
        
        # draw snake for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
            
        # refresh screen 
        screen.title(f"Snake Game. Score:{score}")
        screen.update()
        
        # rinse and repeat
        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False
    
def get_random_food_pos():
    x = random.randint(-WIDTH/ 2 + FOOD_SIZE, WIDTH/ 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT/ 2 + FOOD_SIZE, HEIGHT/ 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1)**2 + (x2-x1)**2)** 0.5 # pythagoras theorem
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos) 
    game_loop()

# Creating a window where we will be doing our dawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # setting the dimensions of the turtle graphic window
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # turn of automatic automation

#Event handlers
screen.listen()
bind_direction_keys()

# creating a turtle to do the bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# food 
food = turtle.Turtle()
food.shape ("circle")
food.color("red")
food.shapesize(FOOD_SIZE/ 20)
food.penup()

# set animation in motion
reset()

# Finish Nicely
turtle.done()