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

def find_rolls_for_removal(array: list[list[str]]) -> tuple[int, int]:
    rolls_for_removal = []

    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] != "@":
                continue

            number_of_surrounding_rolls = count_surrounding_rolls(array, x, y)
            if number_of_surrounding_rolls < 4:
                rolls_for_removal.append((x, y))
    
    return rolls_for_removal

def remove_rolls(array: list[list[str]], rolls_for_removal: list[tuple[int, int]]) -> None:
    for x, y in rolls_for_removal:
        array[x][y] = "."

def main():
    number_of_removed_rolls = 0
    number_of_rounds = 0

    array = read_input_into_2d_array("input.txt")
    while True:
        rolls_for_removal = find_rolls_for_removal(array)
        if len(rolls_for_removal) == 0:
            break

        number_of_removed_rolls += len(rolls_for_removal)
        remove_rolls(array, rolls_for_removal)
        number_of_rounds += 1

    print(f"The sum of removed rolls is: {number_of_removed_rolls}, across {number_of_rounds} rounds")

if __name__ == "__main__":
    main()