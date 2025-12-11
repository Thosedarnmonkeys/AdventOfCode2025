def get_day01_input() -> list[tuple[str, int]]:
    with open("inputs/input01.txt") as f:
        contents = f.readlines()

    rotations = [(line[0], int(line[1:])) for line in contents]
    return rotations


def day01_part1() -> int:
    rotations = get_day01_input()

    zeros = 0
    dial = 50
    for direction, distance in rotations:
        match direction:
            case "L":
                dial = (dial - distance) % 100
            case "R":
                dial = (dial + distance) % 100
            case _:
                raise ValueError(f"Unknown direction: '{direction}'")
        if dial == 0:
            zeros += 1

    return zeros


def day01_part2() -> int:
    rotations = get_day01_input()

    zeros = 0
    dial = 50
    for direction, distance in rotations:
        match direction:
            case "L":
                dial %= -100
                dial = dial - distance
                zeros += dial // -100
            case "R":
                dial = dial + distance
                zeros += dial // 100
            case _:
                raise ValueError(f"Unknown direction: '{direction}'")
        dial %= 100

    return zeros


if __name__ == "__main__":
    answer01_part1 = day01_part1()
    print(answer01_part1)
    answer01_part2 = day01_part2()
    print(answer01_part2)
