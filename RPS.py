# This file was created by Ramzey Insignares
'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = 0
rock_pos_y = 0

# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# setup the paper image using the os module as rock_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the rock
paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the rock_image to the rock_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 300
paper_pos_y = 0

# set the position of the rock_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the rock image using the os module as rock_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the rock
scissors_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = -300
scissors_pos_y = 0

# set the position of the rock_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# function that passes through wn onlick
def someFunction(x, y):
    print("window geometry " + str(cv.winfo_geometry()))
    # screen.setup(WIDTH,HEIGHT,0,0)
    if x > 200 and y > 0 and x < 300 and y < 100:
        print("hitbox!")
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        text.write("hitbox!", False, "left", ("Arial", 24, "normal"))
        # turtle.write(str(x)+","+str(y))
        print(str(x)+","+str(y))
    else: 
        print("not hitbox")
        print(str(x)+","+str(y))
# onclick action runs function on turtle window using x and y coordinates
# https://docs.python.org/3/library/turtle.html#turtle.onclick

screen.onclick(someFunction)
# runs mainloop for Turtle - required to be last
screen.mainloop()




