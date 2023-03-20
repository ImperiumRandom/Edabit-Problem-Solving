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
    if matrix[first_node][second_node] == 1:
        return True

    else:
        return False


def test_function_for_adjacency_matrix():
    # adjacent matrix for 4 points (0-3)
    my_matrix = [[0, 1, 0, 0],
                 [1, 0, 1, 1],
                 [0, 1, 0, 1],
                 [0, 1, 1, 0]]

    user_input = (input('You have four nodes in your matrix please input a number to see if the nodes are adjacent'
                        '\nUserInput: ')).split(',')

    first_user_node = int(user_input[0])

    second_user_node = int(user_input[1])

    if adjacency_matrix_graph(my_matrix, first_user_node, second_user_node):
        print('These nodes are adjacent')

    else:
        print('These nodes are not adjacent')


if __name__ == '__main__':
    print('hello world')

    test_function_for_adjacency_matrix()

    print()

    input()  # pause input
