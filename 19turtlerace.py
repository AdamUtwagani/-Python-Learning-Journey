# from turtle import Turtle, Screen
# import random
# screen = Screen()
# screen.setup(width=500, height=400)
# speed =["slow", "fast", "fastest"]
# random_distance = [2,4,6,8]
# user_bet= screen.textinput(title="Place your Bet", prompt="Which turtle will win ? Enter its color")

# yellowtim = Turtle()
# yellowtim.color("yellow")
# yellowtim.shape("turtle")
# yellowtim.penup()
# yellowtim.speed(random.choice(speed))
# yellowtim.goto(x=-250, y=0)

# bluetim = Turtle()
# bluetim.color("blue")
# bluetim.shape("turtle")
# bluetim.penup()
# bluetim.speed(random.choice(speed))
# bluetim.goto(x=-250, y=80)

# redtim = Turtle()
# redtim.color("red")
# redtim.shape("turtle")
# redtim.penup()
# redtim.speed(random.choice(speed))
# redtim.goto(x=-250, y=-40)

# greentim = Turtle()
# greentim.color("green")
# greentim.shape("turtle")
# greentim.penup()
# greentim.speed(random.choice(speed))
# greentim.goto(x=-250, y=-80)

# purpletim = Turtle()
# purpletim.color("purple")
# purpletim.shape("turtle")
# purpletim.penup()
# purpletim.speed(random.choice(speed))
# purpletim.goto(x=-250, y=40)

# # def startrace():
# #     yellowtim.forward(random.randint(random_distance))
# #     redtim.forward(random.randint(random_distance))
# #     bluetim.forward(random.randint(random_distance))
# #     greentim.forward(random.randint(random_distance))
# #     purpletim.forward(random.randint(random_distance))

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     if yellowtim.xcor() > 230:
#         is_race_on = False
#         winningcolor= yellowtim.pencolor()
#         if winningcolor == user_bet:
#             print("Hurray you have won, The {winningcolor} turtle is the winner")
#         else:
#             print("Sorry you have lost, The {winningcolor} turtle is the winner") 

#     yellowtim.forward(random.randint(random_distance))
#     redtim.forward(random.randint(random_distance))
#     bluetim.forward(random.randint(random_distance))
#     greentim.forward(random.randint(random_distance))
#     purpletim.forward(random.randint(random_distance))

# # screen.listen()
# # screen.onkey(key="space", fun=startrace)
# screen.exitonclick()


# from turtle import Turtle, Screen
# import random

# screen = Screen()
# screen.setup(width=500, height=400)

# colors = ["yellow", "blue", "red", "green", "purple"]
# y_positions = [0, 80, -40, -80, 40]
# speed = ["slow", "fast", "fastest"]
# random_distance = [2, 4, 6, 8]

# user_bet = screen.textinput(title="Place your Bet", prompt="Which turtle will win? Enter its color")

# all_turtles = []

# # Create turtles
# for index in range(5):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[index])
#     tim.penup()
#     tim.speed(random.choice(speed))
#     tim.goto(x=-250, y=y_positions[index])
#     all_turtles.append(tim)

# is_race_on = False

# if user_bet:
#     is_race_on = True

# # Race loop
# while is_race_on:
#     for turtle in all_turtles:
#         turtle.forward(random.choice(random_distance))
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"Hurray you have won! The {winning_color} turtle is the winner.")
#             else:
#                 print(f"Sorry you lost. The {winning_color} turtle is the winner.")

# screen.exitonclick()

from turtle import Turtle, Screen
import random

def setup_turtles(colors, y_positions, speed):
    turtles = []
    for index in range(5):
        tim = Turtle(shape="turtle")
        tim.color(colors[index])
        tim.penup()
        tim.speed(random.choice(speed))
        tim.goto(x=-250, y=y_positions[index])
        turtles.append(tim)
    return turtles

screen = Screen()
screen.setup(width=500, height=400)

colors = ["yellow", "blue", "red", "green", "purple"]
y_positions = [0, 80, -40, -80, 40]
speed = ["slow", "fast", "fastest"]
random_distance = [2, 4, 6, 8]

repeat = True
while repeat:
    # Clear previous turtles and reset screen
    screen.clearscreen()
    screen.setup(width=500, height=400)
    all_turtles = setup_turtles(colors, y_positions, speed)
    user_bet = screen.textinput(title="Place your Bet", prompt="Which turtle will win? Enter its color")
    is_race_on = False

    if user_bet:
        is_race_on = True

    # Race loop
    while is_race_on:
        for turtle in all_turtles:
            turtle.forward(random.choice(random_distance))
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"Hurray you have won! The {winning_color} turtle is the winner.")
                else:
                    print(f"Sorry you lost. The {winning_color} turtle is the winner.")
                break

    again = screen.textinput(title="Play Again?", prompt="Do you want to race again? Type 'yes' or 'no':")
    if not again or again.lower() != "yes":
        repeat = False

screen.bye()