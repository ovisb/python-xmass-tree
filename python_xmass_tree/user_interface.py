from postcard import Postcard
from xmass_tree import XmasTree


class UserInterface:
    def __init__(self, postcard: "Postcard"):
        self.__postcard = postcard

    def start(self) -> None:
        test = self.__get_user_input()
        numbers = [int(number) for number in test.split()]

        if len(numbers) == 2:
            height, interval = numbers

            tree = XmasTree(height, interval)
            tree.print_tree()
            return

        for i in range(0, len(numbers), 4):
            start = i
            height, interval, row, col = numbers[start: start + 4]

            tree = XmasTree(height, interval)

            self.__postcard.add_tree(tree, row, col)

        self.__postcard.print_grid()

    def __get_user_input(self) -> str:
        while True:
            user_input = input()
            if not self.__validate_input(user_input):
                continue
            break

        return user_input

    def __validate_input(self, user_input: str) -> bool:
        numbers = user_input.split()

        for number in numbers:
            if not self.__check_if_valid_digit(number):
                print("Please enter only digits.")
                return False

        if len(numbers) == 2:
            return True

        if not numbers or len(numbers) % 4 != 0:
            print("Please enter multiple of '4' numbers only.")
            return False

        return True

    @staticmethod
    def __check_if_valid_digit(number: str) -> bool:
        try:
            int(number)
            return True
        except ValueError:
            return False
