import random

import config


def ask_for_integer_input(input_str: str, can_be_negative: bool = False, definition_area=None) -> int:
    """
    This function get an input from the user and validates it.
    It ensures it is an int
    """
    while True:
        user_input = input(input_str)

        try:
            user_input = int(user_input)
            if user_input < 0 and not can_be_negative:
                print("Input can be only a positive integer. Try again.")
                continue

            if definition_area and user_input not in definition_area:
                print("Input is not valid. Try again.")
                continue

            break

        except ValueError:
            print("Input must be an integer. Try again")
            continue

    return user_input


def ask_for_n_and_k() -> (int, int):
    n = ask_for_integer_input("Please enter n: ", can_be_negative=False)
    k = ask_for_integer_input("Please enter k: ", can_be_negative=False)
    return n, k


def get_array_values_from_user(n: int) -> [int]:
    arr = []
    for i in range(n):
        num = ask_for_integer_input(f"Please enter the {i+1} number: ", can_be_negative=True)
        arr.append(num)
    return arr


def generate_random_array(n: int) -> [int]:
    arr = []
    for _ in range(n):
        num = random.randint(config.MIN_DEFAULT_VALUE, config.MAX_DEFAULT_VALUE)
        arr.append(num)
    return arr


def ask_user_to_fill_array(n: int) -> [int]:
    input_str = """
1) Enter numbers yourself.
2) Use random numbers.
Your choice is: """
    user_choice = ask_for_integer_input(input_str, definition_area=[1, 2])
    if user_choice == 1:
        arr = get_array_values_from_user(n)
    else:
        arr = generate_random_array(n)
    return arr
