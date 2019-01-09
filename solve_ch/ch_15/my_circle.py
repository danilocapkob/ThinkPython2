#!/bin/python3

import math

class Circle:
    """
    Represents a circle.

    attributes: radius, center.
    """


class Point:
    """
    Represents a point.

    attributes: coordinates x and y.
    """

def point_in_circle(circle, point):
    c_x = circle.center.x
    c_y = circle.center.y
    radius = circle.radius

    p_x = point.x
    p_y = point.y

    distance = math.sqrt((c_x - p_x) ** 2 + (c_y - p_y) ** 2)

    if distance <= radius:
        return True

    return False


def print_circle(circle):
    print("Centro del circulo: (%0.2f, %0.2f)"
            % (circle.center.x, circle.center.y))
    print("Radio: {%0.2f}" % circle.radius)


if __name__ == '__main__':
    cir1 = Circle()
    cir1.center = Point()

    cir1.center.x = 150.0
    cir1.center.y = 100.0
    cir1.radius = 75

    p1 = Point()
    p1.x = float(input("Ingrese la coordenada x del punto: "))
    p1.y = float(input("Ingrese la coordenada y del punto: "))

    result = point_in_circle(cir1, p1)
    print(result)
    print_circle(cir1)
