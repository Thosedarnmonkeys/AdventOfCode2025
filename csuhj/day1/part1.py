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
    count_of_zero_positions = 0
    current_position = 50

    input_data = read_input("input.txt")
    for rotation in input_data:
        current_position = (current_position + get_position_delta(rotation)) % 100
        if current_position == 0:
            count_of_zero_positions += 1
    
    print(f"The number of zero positions visited is: {count_of_zero_positions}")

if __name__ == "__main__":
    main()