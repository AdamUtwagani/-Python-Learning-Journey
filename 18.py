# from turtle import Turtle as t, Screen
# import random
# #modules imports methods 
# #import turtle as _ # alias name 
# #example import turtle as t, t will be defined as turtle 
# #to import all class available in certain module you want 
# #eg: from turtle import *

# timmy = t.Turtle()
# timmy.shape("turtle")
# # timmy.color("Green")
# t.colormode(255)

# def colormode():
#     r= random.randint(0, 255)
#     g= random.randint(0, 255)
#     b= random.randint(0, 255)
#     colorstuple= (r,g,b)
#     return (r,g,b)

# # for _ in range(10):
# #     timmy.forward(10)
# #     timmy.color("white")
# #     timmy.forward(10)
# #     timmy.color("black")


# # for _ in range(4):
# #     timmy.forward(100)
# #     timmy.right(90)

# # for _ in range(5):
# #     timmy.forward(100)
# #     timmy.right(72)

# # for _ in range(6):
# #     timmy.forward(100)
# #     timmy.right(60)    

# # for _ in range(7):
# #     timmy.forward(100)
# #     timmy.right(51) 

# # for _ in range(8):
# #     timmy.forward(100)
# #     timmy.right(45)

# # for _ in range(9):
# #     timmy.forward(100)
# #     timmy.right(40)

# # for _ in range(10):
# #     timmy.forward(100)
# #     timmy.right(36)    

# # timmy.forward(100)
# # timmy.right(90)
# # timmy.forward(100)
# # timmy.right(90)
# # timmy.forward(100)

# colors = ["blue", "Yellow", "green", "red"]
# directions= [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")

# for _ in range (500):
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     timmy.color(colormode())
#     # timmy.color(random.choice(colors))
#     # timmy.width(random.choice(widthsize))
#     # timmy.width = widthsize =+1

# screen = Screen()
# screen.exitonclick()

import turtle
import random

# Create turtle
timmy = turtle.Turtle()
turtle.colormode(255)


# Random RGB color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.shape("arrow")
# timmy.pensize(15)
timmy.speed("fastest")

def draw_spiral(sixe_of_gap):
    for _ in range (int(360 / sixe_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        currentheading= timmy.heading()
        timmy.setheading(currentheading + sixe_of_gap)

draw_spiral(5)




# Directions for the random walk
# directions = [0, 90, 180, 270]

# # Random walk loop
# for _ in range(1000):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# Keep window open until click
screen = turtle.Screen()
screen.exitonclick()














