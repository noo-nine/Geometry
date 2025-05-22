import turtle
def draw_square(ws, length):
    for _ in range(4):
        ws.forward(length)
        ws.right(90)

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a = b
        b = a + b
    sequence = sequence[1:]
    return sequence

def draw_fibonacci_squares(n_squares):
    seq = fibonacci(n_squares)
    ws = turtle.Turtle()
    for i in range(n_squares):
        draw_square(ws, seq[i])
        ws.forward(seq[i])
        ws.left(90)
    turtle.done()

draw_fibonacci_squares(10)