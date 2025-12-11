def get_day03_input() -> list[tuple[int, ...]]:
    with open("inputs/input03.txt") as f:
        contents = f.readlines()

    banks = [tuple([int(battery) for battery in line.strip()]) for line in contents]
    return banks


def day03_part1() -> int:
    banks = get_day03_input()

    total_joltage = 0
    for bank in banks:
        highest_battery = max(bank)
        highest_position = bank.index(highest_battery)
        if highest_position == len(bank) - 1:
            second_battery = highest_battery
            highest_battery = max(bank[:-1])
        else:
            second_battery = max(bank[highest_position + 1:])
        max_joltage = highest_battery * 10 + second_battery
        total_joltage += max_joltage
    
    return total_joltage


def day03_part2() -> int:
    banks = get_day03_input()

    total_joltage = 0
    for bank in banks:
        digits = []
        for i in range(11, -1, -1):
            searchable = bank[:len(bank) - i]
            highest_battery = max(searchable)
            highest_position = searchable.index(highest_battery)
            digits.append(highest_battery)
            bank = bank[highest_position + 1:]
        max_joltage = int("".join(str(x) for x in digits))
        total_joltage += max_joltage

    return total_joltage


if __name__ == "__main__":
    answer03_part1 = day03_part1()
    print(answer03_part1)
    answer03_part2 = day03_part2()
    print(answer03_part2)
