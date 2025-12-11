import itertools


def get_day02_input() -> list[tuple[int, int]]:
    with open("inputs/input02.txt") as f:
        contents = f.read()

    ranges_as_str = [tuple(rnge.split("-")) for rnge in contents.split(",")]
    ranges = [(int(first), int(last)) for first, last in ranges_as_str]
    return ranges


def day02_part1() -> int:
    ranges = get_day02_input()

    total = 0
    for first, last in ranges:
        for id_ in range(first, last + 1):
            id_as_str = str(id_)
            half_length = len(id_as_str) // 2
            if id_as_str[:half_length] == id_as_str[half_length:]:
                total += id_
    return total


def comprises_repeats_of_length(text: str, length: int) -> bool:
    """Check whether the given text consists of repeated strings of the given length."""
    try:
        return len(set(itertools.batched(text, length, strict=True))) == 1
    except ValueError:  # raised if final batch is shorter than length (ie text can't be split exactly into strings of the given length)
        return False


def day02_part2() -> int:
    ranges = get_day02_input()

    total = 0
    for first, last in ranges:
        for id_ in range(first, last + 1):
            id_as_str = str(id_)
            for i in range(len(id_as_str) // 2):  # repeated pattern can't be longer than half the length of the ID
                if comprises_repeats_of_length(id_as_str, i + 1):
                    total += id_
                    break

    return total


if __name__ == "__main__":
    answer02_part1 = day02_part1()
    print(answer02_part1)
    answer02_part2 = day02_part2()
    print(answer02_part2)
