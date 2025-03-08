import turtle

color_list = [(246, 242, 235), (248, 242, 245), (240, 246, 242), (239, 242, 247), (198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), (231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40), (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180), (174, 194, 209), (110, 130, 147), (108, 134, 142), (185, 195, 196)]

from random import choice
from turtle import Turtle
t = Turtle()
turtle.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(320)
t.setheading(0)

for y in range(10):
    for x in range(10):
        t.dot(20, choice(color_list))
        t.forward(50)
    t.setx(t.xcor() - 550)
    t.sety(t.ycor() + 50)
    t.forward(50)

turtle.Screen().exitonclick()