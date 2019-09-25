"""
print shapes: getting input from users
"""


def right_facing_triangle():
    size = int(input("Please input number for size of triangle "))
    for x in range(size + 1):
        print("*" * x)
    for x in range(size - 1, -1, -1):
        print("*" * x)


def right_angled_triangle():
    size = int(input("Please input number for size of triangle "))
    for x in range(size + 1):
        print("*" * x)


def kite():
    size = int(input("Please input number for size "))
    for x in range(1, size + 2, 2):
        print("*" * x)
    for x in range(size - 2, -2, -2):  # TODO: problem here some with some input test cases only work for 5
        print("*" * x)


def rectangle():
    width = int(input("Please input rectangle width "))
    height = int(input("Please input rectangle height "))
    for x in range(height):
        print("*" * width)


def user_choice():
    print("1. Right facing Triangle \n"
          "2. Right angled Triangle \n"
          "3. Kite \n"
          "4. Rectangle ")
    usr_input = int(input("Select one option "))
    if usr_input == 1:
        right_facing_triangle()
    elif usr_input == 2:
        right_angled_triangle()
    elif usr_input == 3:
        kite()
    elif usr_input == 4:
        rectangle()
    else:
        print("Wrong Choice Select from given options!")


user_choice()
