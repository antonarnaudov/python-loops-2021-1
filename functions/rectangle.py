import turtle as t


def draw_rectangle(a, b, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for i in range(1, 3):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)

    t.end_fill()
    t.penup()


draw_rectangle(300, -300, 'green')
