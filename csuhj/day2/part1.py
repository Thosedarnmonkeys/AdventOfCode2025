import string


def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().strip().split(',')
    return data

def get_range(range_string: str) -> tuple[int, int]:
    range_parts = range_string.split('-')
    if len(range_parts) != 2:
        raise ValueError(f"Invalid range string: {range_string}")

    return int(range_parts[0]), int(range_parts[1])

def is_invalid(id: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 != 0:
        return False
    
    mid_index = len(id_str) // 2
    if id_str[0:mid_index] == id_str[mid_index:]:
        return True

    return False

def main():
    sum_of_invalid_ids = 0

    input_data = read_input("input.txt")
    for range_string in input_data:
        min, max = get_range(range_string)

        for i in range(min, max + 1):
            if is_invalid(i):
                sum_of_invalid_ids += i
    
    print(f"The sum of invalid IDs is: {sum_of_invalid_ids}")

if __name__ == "__main__":
    main()