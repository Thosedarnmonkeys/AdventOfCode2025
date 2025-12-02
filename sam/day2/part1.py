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
        if length % 2 == 0:
            halfway = int(length/2)
            if curr_string[:halfway] == curr_string[halfway:]:
                invalid_id_sum += current

print(invalid_id_sum)


