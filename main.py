import math
import sys


def print_hi(name):
    print(f'Hi, {name}')


def add_two_integers(int1, int2):
    return int1 + int2


def minutes_to_seconds(minutes):
    seconds_in_a_minute = 60

    seconds = minutes * seconds_in_a_minute

    return seconds


def is_circle_circumference_greater_than_square_radius(circle_radius, square_radius):
    circumference_of_circle = (2 * math.pi) * circle_radius

    perimeter_of_square = math.sqrt(square_radius) * 4

    if circumference_of_circle > perimeter_of_square:
        return True

    elif perimeter_of_square > circumference_of_circle:
        return False


if __name__ == '__main__':
    print_hi('PyCharm')

    circle_radius = 2

    square_area = 340

    print('Is the circumference greater than the radius?\n')
    print('Answer: ', is_circle_circumference_greater_than_square_radius(circle_radius, square_area))

    # quick pause
    input()
