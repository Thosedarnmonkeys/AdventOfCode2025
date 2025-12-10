from typing import Callable


def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def read_input_into_2d_array(file_path) -> list[list[str]]:
    lines = read_input(file_path)
    array = [[] for _ in lines]

    last_column_separator_index = 0
    for column_index in range(len(lines[0])):
        if all(line[column_index] == " " for line in lines):
            for index, line in enumerate(lines):
                array[index].append(line[last_column_separator_index:column_index])
            last_column_separator_index = column_index + 1

    for index, line in enumerate(lines):
        array[index].append(line[last_column_separator_index:])

    return array

def pivot_numbers(number_strings: list[str]) -> list[int]:
    number_of_columns = len(number_strings[0])
    pivoted_number_strings = ["" for _ in range(number_of_columns)]
    for column_index in range(number_of_columns - 1, -1, -1):
        for number_string in number_strings:
            pivoted_number_strings[column_index] += number_string[column_index]
        
    return list(int(n) for n in pivoted_number_strings)

def calculate_problem(func: Callable[[int, int], int], number_strings: list[str]) -> int:
    numbers = pivot_numbers(number_strings)
    running_total = numbers[0]
    for n in numbers[1:]:
        running_total = func(n, running_total)

    return running_total

def main():
    grand_total = 0

    array = read_input_into_2d_array("input.txt")
    number_of_rows = len(array)
    for column_index in range(len(array[0])):
        operation = array[number_of_rows - 1][column_index].strip()

        number_strings = []
        for row_index in range(number_of_rows - 1):
            num = array[row_index][column_index]
            number_strings.append(num)

        if operation == "*":
            func = lambda x, y: x * y
        else:
            func = lambda x, y: x + y
        
        grand_total += calculate_problem(func, number_strings)
    
    print(f"The grand total of the cephalopod sum is: {grand_total}")

if __name__ == "__main__":
    main()