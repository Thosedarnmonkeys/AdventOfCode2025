def get_day07_input() -> list[list[str]]:
    with open("inputs/input07.txt") as f:
        contents = f.read().splitlines()

    tachyon_manifold = [[char for char in line.strip()] for line in contents]
    return tachyon_manifold


START = "S"
SPLITTER = "^"


def day07_part1() -> int:
    tachyon_manifold = get_day07_input()
    row_length = len(tachyon_manifold[0])

    total_splits = 0
    beams = [True if x == START else False for x in tachyon_manifold[0]]
    for row in tachyon_manifold[1:]:
        new_beams = [False for _ in range(row_length)]
        for pos, is_beam in enumerate(beams):
            if not is_beam:
                continue
            if row[pos] == SPLITTER:
                total_splits += 1
                new_beams[pos - 1] = True
                new_beams[pos + 1] = True
            else:
                new_beams[pos] = True
        beams = new_beams

    return total_splits


def day07_part2():
    tachyon_manifold = get_day07_input()
    row_length = len(tachyon_manifold[0])

    beams = [1 if x == START else 0 for x in tachyon_manifold[0]]
    for row in tachyon_manifold[1:]:
        new_beams = [0 for _ in range(row_length)]
        for pos, count in enumerate(beams):
            if count == 0:
                continue
            if row[pos] == SPLITTER:
                new_beams[pos - 1] += count
                new_beams[pos + 1] += count
            else:
                new_beams[pos] += count
        beams = new_beams

    return sum(beams)


if __name__ == "__main__":
    answer07_part1 = day07_part1()
    print(answer07_part1)
    answer07_part2 = day07_part2()
    print(answer07_part2)
