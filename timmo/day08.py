import math


def get_day08_input() -> list[tuple[int, int, int]]:
    with open("inputs/input08.txt") as f:
        contents = f.read().splitlines()

    coordinates = [(int(x), int(y), int(z)) for x, y, z in [line.strip().split(",") for line in contents]]

    return coordinates


def calculate_smallest_distances(coordinates: list[tuple[int, int, int]], limit: int) -> list[tuple[float, int, int]]:
    """Find the pairs of coordinates with the smallest distance between them."""
    smallest_distances = []
    for i, box1 in enumerate(coordinates[:-1]):
        x1, y1, z1 = box1
        new_distances = []
        for j, box2 in enumerate(coordinates[i + 1:], start=i + 1):
            x2, y2, z2 = box2
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
            new_distances.append((distance, i, j))
        smallest_distances = sorted(smallest_distances + new_distances)[:limit]
    return smallest_distances


def connect_pairs(pairs: list[tuple[int, int]], total: int) -> dict[int, set[int]]:
    """Connect pairs of boxes to form circuits."""
    state = {i: i for i in range(total)}
    circuits = {i: {i} for i in range(total)}

    for box1, box2 in pairs:
        circuit_idx1, circuit_idx2 = state[box1], state[box2]
        if circuit_idx1 == circuit_idx2:
            continue

        circuit1, circuit2 = circuits[circuit_idx1], circuits[circuit_idx2]
        circuit1.update(circuit2)
        for box in circuit2:
            state[box] = circuit_idx1
        circuits.pop(circuit_idx2)

    return circuits


def day08_part1() -> int:
    coordinates = get_day08_input()
    total_boxes = len(coordinates)
    limit = 1000
    largest_n_for_result = 3

    smallest_distances = calculate_smallest_distances(coordinates, limit)
    closest_boxes = [(i, j) for (distance, i, j) in smallest_distances]
    circuits = connect_pairs(closest_boxes, total_boxes)
    sizes = [len(c) for c in circuits.values()]

    return math.prod(sorted(sizes, reverse=True)[:largest_n_for_result])


def calculate_all_distances(coordinates: list[tuple[int, int, int]]) -> list[tuple[float, int, int]]:
    """Calculate the distances between all possible pairs of coordinates."""
    distances = []
    for i, (x1, y1, z1) in enumerate(coordinates[:-1]):
        for j, (x2, y2, z2) in enumerate(coordinates[i + 1:], start=i + 1):
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
            distances.append((distance, i, j))
    return sorted(distances)


def connect_all_boxes(pairs: list[tuple[int, int]], total: int) -> tuple[int, int]:
    """Connect pairs of boxes to form circuits until all boxes are in one connected circuit."""
    state = {i: i for i in range(total)}
    circuits = {i: {i} for i in range(total)}

    for i, (box1, box2) in enumerate(pairs, start=1):
        circuit_idx1, circuit_idx2 = state[box1], state[box2]
        if circuit_idx1 == circuit_idx2:
            continue

        circuit1, circuit2 = circuits[circuit_idx1], circuits[circuit_idx2]
        circuit1.update(circuit2)
        for box in circuit2:
            state[box] = circuit_idx1
        circuits.pop(circuit_idx2)

        if len(circuits) == 1:
            return box1, box2

    else:
        raise ValueError("Expected to exit before connecting all pairs")


def day08_part2():
    coordinates = get_day08_input()
    total_boxes = len(coordinates)

    distances = calculate_all_distances(coordinates)
    pairs = [(i, j) for (distance, i, j) in distances]
    final_pair = connect_all_boxes(pairs, total_boxes)

    final1, final2 = final_pair
    x1, x2 = coordinates[final1][0], coordinates[final2][0]

    return x1 * x2


if __name__ == "__main__":
    answer08_part1 = day08_part1()
    print(answer08_part1)
    answer08_part2 = day08_part2()
    print(answer08_part2)
