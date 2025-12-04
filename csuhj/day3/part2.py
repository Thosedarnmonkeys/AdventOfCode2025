import string


def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def get_max_battery(bank: str, start_index: int, end_index: int) -> tuple[int, int]:
    max_index, max_battery = max(enumerate(bank[start_index:end_index]), key=lambda x: int(x[1]))
    return max_index + start_index, int(max_battery)

def get_joltage_from_bank(bank: str, number_of_batteries: int) -> int:
    joltage_for_bank = 0
    previous_battery_index = -1

    for i in range(1, number_of_batteries + 1):
        battery_index, battery = get_max_battery(bank, previous_battery_index + 1, len(bank) - (number_of_batteries - i))
        joltage_for_bank += battery * (10 ** (number_of_batteries - i))
        previous_battery_index = battery_index

    return joltage_for_bank

def main():
    joltage_sum = 0

    input_data = read_input("input.txt")
    for bank in input_data:
        joltage_sum += get_joltage_from_bank(bank, 12)
    
    print(f"The sum of bank joltages is: {joltage_sum}")

if __name__ == "__main__":
    main()