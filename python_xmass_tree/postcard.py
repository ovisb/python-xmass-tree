from xmass_tree import XmasTree


class Postcard:
    max_height = 30
    max_width = 50

    def __init__(self):
        self.__grid: list[list[str]] = []
        self.__draw_grid()

    def add_tree(self, tree: "XmasTree", row: int, col: int) -> None:
        if not self.__validate_add(tree, row, col):
            return

        for row_t in tree.get_tree:
            half_idx = len(row_t) // 2
            start = 0
            for new_col in range(col - half_idx, col + half_idx + 1):
                character = row_t[start]
                start += 1

                self.__grid[row][new_col] = character
            row += 1

    def print_grid(self) -> None:
        for row in self.__grid:
            for character in row:
                print(character, end="")
            print()

    def __draw_grid(self) -> None:
        for i in range(Postcard.max_height):
            row = []

            if i == 0 or i == Postcard.max_height - 1:
                for _ in range(Postcard.max_width):
                    row.append("-")
                self.__grid.append(row)

                if i == 0:
                    continue
                else:
                    break

            for j in range(Postcard.max_width):
                if j == 0 or j == Postcard.max_width - 1:
                    row.append("|")
                else:
                    row.append(" ")

            self.__grid.append(row)

        self.__set_tree_message()

    def __set_tree_message(self) -> None:
        message = "Merry Xmas"
        half_total_width = Postcard.max_width // 2
        half_message_length = len(message) // 2
        start = half_total_width - half_message_length
        end = half_total_width + half_message_length

        message_index = 0
        for col in range(start, end):
            self.__grid[27][col] = message[message_index]
            message_index += 1

    def __validate_add(self, tree, row, col) -> bool:
        return all(
            [
                self.__check_tree_height(tree.height),
                self.__check_tree_height_with_line(tree.height, row),
                self.__check_tree_width(tree, col),
            ]
        )

    def __check_tree_height(self, height: int) -> bool:
        if height < 0 or height > self.max_height - 1:
            print("Tree insert failed. Tree can only have a max height of 28.")
            return False

        return True

    def __check_tree_height_with_line(self, height: int, row: int) -> bool:
        if height + row > self.max_height - 1 or row < 1:
            print("Tree insert failed. Tree exceeds current grid.")
            return False
        return True

    def __check_tree_width(self, tree, col: int) -> bool:
        before_last = tree.get_tree[-2]
        if (len(before_last) // 2) + col > self.max_width - 2:
            print("Tree insert failed. Leaf width exceeds right grid.")
            return False

        if col - (len(before_last) // 2) < 1:
            print("Tree insert failed. Leaf width exceeds left grid.")
            return False

        return True
