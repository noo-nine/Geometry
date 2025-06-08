import turtle
import math

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        sequence.append(a)
    return sequence

factor = int(input("Enter the factor: "))
def draw_fibonacci_spiral(n):
    seq = fibonacci(n)
    ws = turtle.Turtle()

    # first square needs 4 sides
    ws.forward(seq[0] * factor)
    ws.left(90)
    ws.forward(seq[0] * factor)
    ws.left(90)
    ws.forward(seq[0] * factor)
    ws.left(90)
    ws.forward(seq[0] * factor)
    
    # for the remaining squares
    for i in range(1, n):
        ws.backward(seq[i - 1] * factor)
        ws.right(90)
        ws.forward(seq[i] * factor)
        ws.left(90)
        ws.forward(seq[i] * factor)
        ws.left(90)
        ws.forward(seq[i] * factor)

    # setting the turtle at right position to draw the spiral
    ws.penup()
    ws.setposition(factor, 0) # starting point of the spiral is the last point of the first square drawn
    ws.seth(0) # setting the angle to 0 ( facing right )
    ws.pendown()
    ws.pencolor("blue")

    # divide the quarter arc need to be drawn in each square into 90 parts
    ws.left(90)
    for i in range(n):
        step = math.pi * seq[i] * factor / 2
        step = step / 90
        for j in range(90):
            ws.forward(step)
            ws.left(1)
    
    turtle.done()

n_fibo = int(input("Enter the a number greater than 1: "))
draw_fibonacci_spiral(n_fibo)