import turtle

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        sequence.append(a)
    return sequence

factor = int(input("Enter the factor: "))
def draw_fibonacci_skeleton(n_squares):
    seq = fibonacci(n_squares)
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
    for i in range(1, n_squares):
        ws.backward(seq[i - 1] * factor)
        ws.right(90)
        ws.forward(seq[i] * factor)
        ws.left(90)
        ws.forward(seq[i] * factor)
        ws.left(90)
        ws.forward(seq[i] * factor)
    
    turtle.done()

draw_fibonacci_skeleton(10)