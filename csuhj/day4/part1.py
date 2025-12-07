import string


def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def read_input_into_2d_array(file_path) -> list[list[str]]:
    array = []
    for line in read_input(file_path):
        array.append(list(line))

    return array

def count_surrounding_rolls(array: list[list[str]], x: int, y: int) -> int:
    number_of_surrounding_rolls = 0
    number_of_surrounding_rolls += 1 if x > 0 and y > 0 and array[x-1][y-1] == '@' else 0
    number_of_surrounding_rolls += 1 if x > 0 and array[x-1][y] == '@' else 0
    number_of_surrounding_rolls += 1 if x > 0 and y < len(array[0]) - 1 and array[x-1][y+1] == '@' else 0
    number_of_surrounding_rolls += 1 if y > 0 and array[x][y-1] == '@' else 0
    number_of_surrounding_rolls += 1 if y < len(array[0]) - 1 and array[x][y+1] == '@' else 0
    number_of_surrounding_rolls += 1 if x < len(array) - 1 and y > 0 and array[x+1][y-1] == '@' else 0
    number_of_surrounding_rolls += 1 if x < len(array) - 1 and array[x+1][y] == '@' else 0
    number_of_surrounding_rolls += 1 if x < len(array) - 1 and y < len(array[0]) - 1 and array[x+1][y+1] == '@' else 0
    return number_of_surrounding_rolls

def main():
    number_of_clear_rolls = 0

    array = read_input_into_2d_array("input.txt")
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] != "@":
                continue

            number_of_clear_rolls += 1 if count_surrounding_rolls(array, x, y) < 4 else 0
    
    print(f"The sum of clear rolls is: {number_of_clear_rolls}")

if __name__ == "__main__":
    main()