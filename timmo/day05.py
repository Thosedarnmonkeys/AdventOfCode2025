def get_day05_input() -> tuple[list[tuple[int, int]], list[int]]:
    with open("inputs/input05.txt") as f:
        contents = f.read().splitlines()

    fresh_ingredient_id_ranges = []
    index = 0  # stop IDE complaining about possible referenced-before-assignment
    for index, line in enumerate(line.strip() for line in contents):
        if not line:
            break
        start, end = line.split("-")
        fresh_ingredient_id_ranges.append((int(start), int(end)))

    available_ingredient_ids = [int(x) for x in contents[index + 1:]]

    return fresh_ingredient_id_ranges, available_ingredient_ids


def day05_part1() -> int:
    fresh_ingredient_id_ranges, available_ingredient_ids = get_day05_input()

    fresh_count = 0
    for ingredient_id in available_ingredient_ids:
        if any(start <= ingredient_id <= end for start, end in fresh_ingredient_id_ranges):
            fresh_count += 1

    return fresh_count


def consolidate_ranges(ranges):
    """Combine any overlapping or adjacent ranges into a single range."""
    ordered_ranges = sorted(ranges)

    new_ranges = []
    start, end = ordered_ranges[0]
    i = 1
    while i < len(ordered_ranges):
        next_start, next_end = ordered_ranges[i]
        if next_start <= end + 1:  # + 1 catches adjacent ranges as well as overlapping ones
            end = max(end, next_end)
        else:
            new_ranges.append((start, end))
            start, end = next_start, next_end
        i += 1
    new_ranges.append((start, end))

    return new_ranges


def day05_part2():
    fresh_ingredient_id_ranges, __ = get_day05_input()
    consolidated_ranges = consolidate_ranges(fresh_ingredient_id_ranges)
    fresh_ingredient_id_count = sum(end - start + 1 for start, end in consolidated_ranges)
    return fresh_ingredient_id_count


if __name__ == "__main__":
    answer05_part1 = day05_part1()
    print(answer05_part1)
    answer05_part2 = day05_part2()
    print(answer05_part2)
