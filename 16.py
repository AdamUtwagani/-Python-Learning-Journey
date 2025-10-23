# Object Oriented Programming (OOP)

# import anothermodule
# print(anothermodule.Greeting)

# from turtle import Turtle, Screen
# Timmy= Turtle()
# Timmy.shape("turtle")
# Timmy.color("green")
# print(Timmy)
# myscreen= Screen()
# print(myscreen.canvheight)
# Timmy.forward(100)
# Timmy.right(100)
# Timmy.left(100)
# Timmy.right(100)
# myscreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Region name",["Arusha", "Dar es salaam", "Dodoma", "Mwanza"])
table.add_column("University name",[ "Arusha Tech", "UDSM", "UDOM","Bugando"])
table.align["Region name"]= "c"
table.align["University name"]= "l"
print(table)

