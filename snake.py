# import turtle graphics module
import turtle

# defining program constants
WIDTH = 600
HEIGHT = 600
DELAY = 20 # milliseconds between screen updates

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

# Creating a window where we will be doin our drwaing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # setting the dimensions of the turtle graphic window
screen.title("Snake Game")
screen.bgcolor("cyan")
screen.tracer(0) # turns off automatic animation

# creating a turtle 
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# giving the turtle commands
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)

# to stop the turtle we will have to use the done method 
turtle.done()