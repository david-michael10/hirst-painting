import random
import turtle

def turn_around():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)

def paint(columns, rows):
    for i in range(rows):
        for _ in range(columns):
            tim.dot(25, random.choice(color_list))
            tim.forward(50)

        turn_around()

        for _ in range(columns):
            tim.forward(50)
        tim.setheading(0)

color_list = [(236, 35, 108), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]

tim = turtle.Turtle()
tim.hideturtle()
screen = turtle.Screen()
turtle.colormode(255)

tim.speed("fastest")
tim.penup()
tim.teleport(-240,-240)

paint(10,10)

screen.exitonclick()