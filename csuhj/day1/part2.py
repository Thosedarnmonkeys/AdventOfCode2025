import string


def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def get_position_delta(rotation: string):
    direction = rotation[0]
    steps = int(rotation[1:])
    if direction == 'R':
        return steps
    elif direction == 'L':
        return -steps
    else:
        raise ValueError(f"Invalid rotation: {rotation}")

def main():
    count_of_passing_zero_positions = 0
    current_position = 50

    input_data = read_input("input.txt")
    for rotation in input_data:
        position_delta = get_position_delta(rotation)
        full_rotations = abs(position_delta) // 100
        remainder_rotation = abs(position_delta) % 100

        passed_zero_on_remainder = 1 if (
            current_position != 0 and
            ((position_delta < 0 and current_position - remainder_rotation <= 0) or
              (position_delta > 0 and current_position + remainder_rotation >= 100))) else 0

        count_of_passing_zero_positions += full_rotations + passed_zero_on_remainder
        current_position = (current_position + position_delta) % 100

    print(f"The number of zero positions visited is: {count_of_passing_zero_positions}")

if __name__ == "__main__":
    main()