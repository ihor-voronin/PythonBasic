import turtle


def draw_rectangle() -> None:
    turtle.shape("turtle")
    turtle.fd(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.exitonclick()


if __name__ == '__main__':
    draw_rectangle()
