import math


def get_day06_input() -> list[str]:
    with open("inputs/input06.txt") as f:
        contents = f.read().splitlines()

    # IDE strips trailing whitespace from lines; restore to equal lengths
    normalised_length = max(len(line) for line in contents)
    normalised_contents = []
    for line in contents:
        shortfall = normalised_length - len(line.rstrip())
        new_line = line.rstrip() + " " * shortfall
        normalised_contents.append(new_line)

    return normalised_contents


def day06_part1() -> int:
    contents = get_day06_input()
    split_contents = [[x for x in line.split(" ") if x.strip()] for line in contents]
    numbers = [[int(x) for x in line] for line in split_contents[:-1]]
    symbols = split_contents[-1]

    results = []
    for idx, symbol in enumerate(symbols):
        match symbol:
            case "+":
                results.append(sum(line[idx] for line in numbers))
            case "*":
                results.append(math.prod(line[idx] for line in numbers))
            case _:
                raise ValueError(f"Unknown symbol '{symbol}'")

    grand_total = sum(results)
    return grand_total


def transpose_contents(contents: list[str]) -> list[str]:
    """Transpose and reverse the contents.

    Columns from right to left become rows from top to bottom.

    """
    size = len(contents[0])
    transposed = []
    for i in reversed(range(size)):
        new_line = "".join(line[i] for line in contents)
        transposed.append(new_line)
    return transposed


type Problem = tuple[tuple[int, ...], str]


def collate_problems(contents: list[str]) -> list[Problem]:
    """Collate problems."""
    problems = []
    numbers = []
    for line in contents:
        if line.strip() == "":  # check for blank line
            assert not numbers  # occurs immediately after end of problem
            continue

        digits, last = line[:-1], line[-1]
        numbers.append(int(digits))
        if last in ("+", "*"):
            problems.append((tuple(numbers), last))
            numbers = []

    return problems


def solve_problems(problems: list[Problem]) -> list[int]:
    """Perform calculation of collated problems and return results."""
    results = []
    for numbers, symbol in problems:
        match symbol:
            case "+":
                results.append(sum(numbers))
            case "*":
                results.append(math.prod(numbers))
            case _:
                raise ValueError(f"Unknown symbol '{symbol}'")
    return results


def day06_part2():
    contents = get_day06_input()
    transposed_contents = transpose_contents(contents)
    problems = collate_problems(transposed_contents)
    results = solve_problems(problems)
    grand_total = sum(results)
    return grand_total


if __name__ == "__main__":
    answer06_part1 = day06_part1()
    print(answer06_part1)
    answer06_part2 = day06_part2()
    print(answer06_part2)
