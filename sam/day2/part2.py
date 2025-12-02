def check_if_match(num_str: str, str_len: int, pattern_len: int) -> bool:
    pattern = num_str[:pattern_len]
    position = pattern_len
    while position < str_len:
        candidate = curr_string[position:position+partLength]
        if pattern != candidate:
            return False
        
        position += pattern_len

    return True

invalid_id_sum = 0
filepath = "input.txt"
file = open(filepath)
line = file.readline()

id_ranges = line.split(",")
for id_range in id_ranges:
    array = id_range.split("-")
    lower = int(array[0])
    upper = int(array[1])
    
    for current in range(lower, upper + 1):
        curr_string = str(current)
        length = len(curr_string)

        for i in range(2, length + 1):
            if length % i == 0:
                partLength = int(length / i)
                if check_if_match(curr_string, length, partLength):
                    invalid_id_sum += current
                    break

print(invalid_id_sum)


