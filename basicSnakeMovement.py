# import turtle graphics module
import turtle

# defining program constants
WIDTH = 600
HEIGHT = 600
DELAY = 400 # milliseconds

def move_snake():
    stamper.clearstamps() # remove existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += 20 
    
    # add new head to snake body
    snake.append(new_head)
    
    # remove last segment of snake
    snake.pop(0)
    
    # draw snake for the first time.
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
        
    # refresh screen 
    screen.update()
    
    # rinse and repeat
    turtle.ontimer(move_snake, DELAY)

    
# Creating a window where we will be doing our dawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # setting the dimensions of the turtle graphic window
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # turn of automatic automation

# creating a turtle to do the bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# creating snake as a list of coordiante pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# draw snake for the first time.
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
# set animation in motion
move_snake()

# Finish Nicely
turtle.done()