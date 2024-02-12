class XmasTree:
    def __init__(self, height: int, number_of_decorations: int) -> None:
        self.__height = height
        self.__number_of_decorations = number_of_decorations
        self.__tree: list[list[str]] = []
        self.__generate_tree()

    def __add_leaf_start_end(self) -> None:
        for i in range(2, len(self.__tree) - 1):
            self.__tree[i][0] = "/"
            self.__tree[i][-1] = "\\"

    def __add_decorations(self) -> None:
        current = 0
        for i in range(2, len(self.__tree)):
            start = 0
            for j in range(1, len(self.__tree[i]) - 1):
                if start % 2 == 1:
                    if current % self.__number_of_decorations == 0:
                        self.__tree[i][j] = "O"
                    current += 1
                start += 1

    def __generate_tree(self) -> None:
        start_num = 3
        for t in ("X", "^"):
            row = [t]
            self.__tree.append(row)

        for i in range(2, self.__height + 1):
            row = []
            for _ in range(start_num):
                row.append("*")
            self.__tree.append(row)
            start_num += 2

        final = ("|", " ", "|")
        row = []
        for char in final:
            row.append(char)
        self.__tree.append(row)

        self.__add_leaf_start_end()
        self.__add_decorations()

    def print_tree(self) -> None:
        for i, row in enumerate(self.__tree, start=1):
            if i == 1:
                print(" " * (len(self.__tree) - 3), end="")
            elif i == len(self.__tree):
                print(" " * (len(self.__tree) - 4), end="")
            else:
                print(" " * (len(self.__tree) - i - 1), end="")
            for character in row:
                print(character, end="")
            print()

    @property
    def get_tree(self) -> list[list[str]]:
        return self.__tree

    @property
    def height(self) -> int:
        return self.__height
