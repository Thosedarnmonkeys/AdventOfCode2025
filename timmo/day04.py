def get_day04_input() -> list[str]:
    with open("inputs/input04.txt") as f:
        contents = f.read().splitlines()

    return contents


PAPER = "@"
EMPTY = "."


class Grid:
    def __init__(self, contents: list[str]) -> None:
        self.contents = contents
        self.width = len(self.contents[0])
        self.height = len(self.contents)

        assert all(len(row) == self.width for row in self.contents)

    def get_cell(self, x: int, y: int) -> str | None:
        """Retrieve the value of the cell at the given position.

        (0,0) is at the top-left corner of the grid.
        Return `None` if the coordinates are outside the grid.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.contents[y][x]

    def get_surrounding_cells(self, x: int, y: int) -> tuple[str, ...]:
        """Retrieve the values in the cells surrounding the given one.

        Return at most 8 values (fewer will be returned for a cell at an edge or corner).
        """
        cells = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                x_target = x + i
                y_target = y + j
                if (value := self.get_cell(x_target, y_target)) is not None:
                    cells.append(value)
        return tuple(cells)

    def set_cell(self, x: int, y: int, value: str) -> None:
        """Set the cell at the given position to the given value.

        Has no effect if the coordinates are outside the grid.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        current_row = self.contents[y]
        new_row = current_row[:x] + value + current_row[x + 1:]
        self.contents[y] = new_row


def day04_part1() -> int:
    contents = get_day04_input()
    grid = Grid(contents)

    accessible_rolls_count = 0
    for j in range(grid.height):
        for i in range(grid.width):
            if grid.get_cell(i, j) == EMPTY:
                continue
            surrounding_cells = grid.get_surrounding_cells(i, j)
            if len([cell for cell in surrounding_cells if cell == PAPER]) < 4:
                accessible_rolls_count += 1

    return accessible_rolls_count


def day04_part2() -> int:
    contents = get_day04_input()
    grid = Grid(contents)

    rolls_removed = 0

    while True:
        accessible_rolls = []
        for i in range(grid.width):
            for j in range(grid.height):
                if grid.get_cell(i, j) == EMPTY:
                    continue
                surrounding_cells = grid.get_surrounding_cells(i, j)
                if sum(cell == PAPER for cell in surrounding_cells) < 4:
                    accessible_rolls.append((i, j))

        if len(accessible_rolls) == 0:
            break

        for x, y in accessible_rolls:
            grid.set_cell(x, y, EMPTY)
            rolls_removed += 1

    return rolls_removed


if __name__ == "__main__":
    answer04_part1 = day04_part1()
    print(answer04_part1)
    answer04_part2 = day04_part2()
    print(answer04_part2)
