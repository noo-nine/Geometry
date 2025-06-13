import turtle
import matplotlib.pyplot as plt
import math
import time

# user input
no_of_sides = int(input("Enter the number the polygons you want to display: "))

screen = turtle.Screen()
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()

radius = 300

pen.penup()
pen.goto(0, -radius)
pen.pendown()
pen.circle(radius)
pen.penup()
pen.goto(0, radius)
pen.pendown()

def polygons(n_sides):
    for n in range(2, n_sides):
        points = []
        angle = 360 / n
        pen.seth(180)
        # marking the points
        for i in range(n):
            points.append(pen.position())
            pen.circle(radius, angle)
            pen.dot(6, 'red')
        print(points)

        # drawing a polygon
        pen.pencolor('blue')
        pos = 0
        for point in points:
            pen.goto(points[pos])
            pos += 1
        pen.goto(points[0])

        screen.update()
        time.sleep(0.5)

    screen.mainloop()

polygons(no_of_sides)