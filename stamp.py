# import turtle graphics module
import turtle

# defining program constants
WIDTH = 600
HEIGHT = 600

# Creating a window where we will be doing our dawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # setting the dimensions of the turtle graphic window
screen.title("Stamping")
screen.bgcolor("cyan")

# creating a turtle 
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("blue")
stamper.shapesize(50/20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10/20)
stamper.goto(100, 100)
stamper.stamp

# to stop the turtle we will have to use the done method 
turtle.done()