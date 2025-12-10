def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def read_input_into_2d_array(file_path) -> list[list[str]]:
    array = []
    for line in read_input(file_path):
        array.append(line.split())

    return array

def main():
    grand_total = 0

    array = read_input_into_2d_array("input.txt")
    number_of_rows = len(array)
    for column_index in range(len(array[0])):
        operation = array[number_of_rows - 1][column_index]
        running_total = int(array[0][column_index])
        for row_index in range(1, number_of_rows - 1):
            if operation == "*":
                running_total *= int(array[row_index][column_index])
            else:
                running_total += int(array[row_index][column_index])
        grand_total += running_total
    
    print(f"The grand total of the cephalopod sum is: {grand_total}")

if __name__ == "__main__":
    main()