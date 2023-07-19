# import turtle graphics module
import turtle

# defining program constants
WIDTH = 600
HEIGHT = 600
DELAY = 100 # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
        
def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
        
def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
        
def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def game_loop():
    stamper.clearstamps() # remove existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
    
    #check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.bye()
    else:
        
    
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
        turtle.ontimer(game_loop, DELAY)

    
# Creating a window where we will be doing our dawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # setting the dimensions of the turtle graphic window
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # turn of automatic automation

#Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# creating a turtle to do the bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# creating snake as a list of coordiante pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# draw snake for the first time.
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
# set animation in motion
game_loop()

# Finish Nicely
turtle.done()