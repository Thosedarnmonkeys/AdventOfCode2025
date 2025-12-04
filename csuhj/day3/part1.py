import string


def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def get_max_battery(bank: str, start_index: int, end_index: int) -> tuple[int, int]:
    max_battery = 0
    max_index = -1

    for index, battery in enumerate(int(battery) for battery in list(bank[start_index:end_index])):
        if battery > max_battery:
            max_battery = battery
            max_index = index
    
    return max_index, max_battery

def get_joltage_from_bank(bank: str) -> int:

    first_battery_index, first_battery = get_max_battery(bank, 0, len(bank) - 1)
    _, second_battery = get_max_battery(bank, first_battery_index + 1, len(bank))
    return (first_battery * 10) + second_battery

def main():
    joltage_sum = 0

    input_data = read_input("input.txt")
    for bank in input_data:
        joltage_sum += get_joltage_from_bank(bank)
    
    print(f"The sum of bank joltages is: {joltage_sum}")

if __name__ == "__main__":
    main()