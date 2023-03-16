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

def test_function_for_circumference_and_radius():
    print_hi('PyCharm')

    circle_radius = 2

    square_area = 340

    print('Is the circumference greater than the radius?\n')
    print('Answer: ', is_circle_circumference_greater_than_square_radius(circle_radius, square_area))

    # quick pause
    input()


def adjacency_matrix_graph(matrix, first_node, second_node):
    print("check index's of matrix with parameters")







if __name__ == '__main__':
    print('hello world')

    # adjacent matrix for 4 points (0-3)
    my_matrix = [[0,1,0,0]
             ,[1,0,1,1]
             ,[0,1,0,1]
             ,[0,1,1,0]]

    adjacency_matrix_graph(my_matrix, 1, 3)

