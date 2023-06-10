import math
import os


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


def food_catagory_storage(f_fridge):
    os.system("cls")

    user_input = "7"  # defined as num initially for while loop validation
    selection = 0

    # main function loop
    while True:

        os.system("cls")

        # initial continue or back selection
        while True:
            user_input = input("please enter 1 to store food, or 2 to go back to main menu: ")
            if user_input.isdigit():
                if int(user_input) == 1 or int(user_input) == 2:
                    break

        os.system("cls")

        selection = int(user_input)

        # returns to main menu
        if selection == 2:
            return

        # enters category name

        for key, values in f_fridge.items():
            print(key, ": ")
            for listValues in values:
                print(listValues)
            print()  # space

        print()  # space

        user_input = input("please enter the name of your category or (/back) to exit back to selection: ")

        if user_input == "/back":
            pass

        else:
            current_catagory = user_input

            f_fridge[current_catagory] = []

        os.system("cls")

        # displays and allows for data to be changed
        while True:

            if user_input == "/back":
                break

            os.system("cls")

            print("Your current category: ", current_catagory)

            for values in f_fridge[current_catagory]:
                print(values)

            print()

            user_input = input("now please enter foods that you want to add, any food will do, type (/end) to stop,"
                               " type (/main) to return to main menu: ")

            if user_input == "/end":
                break

            elif user_input == "/main":
                return

            else:
                f_fridge[current_catagory].append(user_input)


def food_catagory_test():
    user_choice = 0
    fridge = {}

    while True:
        print('hello world')

        os.system("cls")

        food_catagory_storage(fridge)

        os.system("cls")

        while True:
            user_choice = input("please enter 1 to go back to first function, or 2 to exit")
            if user_choice.isdigit() and int(user_choice) == 1 or 2:
                break
            else:
                continue

        if int(user_choice) == 1:
            continue
        else:
            break


def length_of_a_line_segment(segment_1, segment_2):
    line_length = math.sqrt(math.pow((segment_2[1]-segment_1[1]), 2) + math.pow((segment_2[0] - segment_1[0]), 2))
    return round(line_length, 2)






if __name__ == '__main__':

    print(length_of_a_line_segment([15, 7], [22, 11]))
