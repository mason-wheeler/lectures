from turtle import Turtle

def regular_polygon(t: Turtle, length: int, num_sides=4) -> None:
    """
    Draw any polygon with a given length.
    :param t:  an instance of a turtle used to render
    :param length: the length of one side of the polygon
    :param num_sides: number of sides
    :return: None
    """
    for count in range(num_sides):
        t.forward(length)
        t.left(360/num_sides)


def square(t: Turtle, length: int) -> None:
    """
    Draw a square with a given length
    :param t: an instance of a turtle used to render
    :param length: the length of one side of a square
    :return: None
    """
    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t: Turtle, length: int) -> None:
    """
    Draw a hexagon with a given length
    :param t: an instance of a turtle used to render
    :param length: the length of one side of a hexagon
    :return: None
    """
    for count in range(6):
        t.forward(length)
        t.left(60)


def triangle(t: Turtle, length: int) -> None:
     """
     Draw a triangle with a given length
     :param t: an instance of a turtle used to render
     :param length: the length of one side of a triangle
     :return: None
     """
     for count in range(3):
         t.forward(length)
         t.left(120)


def octagon(t: Turtle, length: int) -> None:
    """
    Draw a octagon with a given length
    :param t: an instance of a turtle used to render
    :param length: the length of one side of a octagon
    :return: None
    """
    for count in range(8):
        t.forward(length)
        t.left(45)


def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:
    """
    Draws a radial pattern of n shapes with the given length.
    :param t: a Turtle instance
    :param n: number of shapes
    :param length: length of shape side
    :param shape: a function for drawing some shape
    :return: none
    """
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


def test_module() ->None:
    a_turtle = Turtle()
    screen = Screen()
    radial_pattern(a_turtle, n=10, length=50, shape=square)
    sleep(10)   # pause for 5 seconds


if __name__ == '__main__':
    main()