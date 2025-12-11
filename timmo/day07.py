def get_day07_input() -> list[list[str]]:
    with open("inputs/input07.txt") as f:
        contents = f.read().splitlines()

    tachyon_manifold = [[char for char in line.strip()] for line in contents]
    return tachyon_manifold


class State:
    START = "S"
    SPLITTER = "^"
    BEAM = "|"


def trace_paths(current_row: list[str], previous_row: list[str]) -> tuple[int, list[str]]:
    """Calculate the paths traced by beams."""
    traced_row = [char for char in current_row]  # start with copy of current row
    splits = 0

    for i, (above, this) in enumerate(zip(previous_row, current_row)):
        # `this` might not match 'current state' ie what's in `traced_row`
        # specifically if we just split a beam and put one 'ahead' (to the right)
        # but this doesn't matter as we're only interested in whether `this` is a splitter
        # moreover, we're writing the changed state into a different variable (`traced_row`)
        # so no issues with modifying something as we iterate over it
        match above:
            case State.START:
                traced_row[i] = State.BEAM
            case State.BEAM:
                if this == State.SPLITTER:
                    splits += 1
                    traced_row[i - 1] = State.BEAM
                    traced_row[i + 1] = State.BEAM
                else:
                    traced_row[i] = State.BEAM

    return splits, traced_row


def day07_part1() -> int:
    tachyon_manifold = get_day07_input()

    total_splits = 0
    previous_row = tachyon_manifold[0]
    for i in range(1, len(tachyon_manifold)):
        current_row = tachyon_manifold[i]
        splits, traced_row = trace_paths(current_row, previous_row)
        total_splits += splits
        previous_row = traced_row

    return total_splits


def day07_part2():
    tachyon_manifold = get_day07_input()
    row_length = len(tachyon_manifold[0])

    beams = [1 if x == State.START else 0 for x in tachyon_manifold[0]]
    for row in tachyon_manifold[1:]:
        new_beams = [0 for _ in range(row_length)]
        for pos, count in enumerate(beams):
            if row[pos] == State.SPLITTER:
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
