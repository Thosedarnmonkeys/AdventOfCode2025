def is_roll(line_i, char_i):
    return 1 if (lines[line_i][char_i] == roll) | (lines[line_i][char_i] == roll_to_remove) else 0

def get_adj_roll_count(i, j, lines_len, row_len):
    adj_rolls = 0

    #above
    if i != 0:
        if j != 0:
            adj_rolls += is_roll(i-1, j-1)

        if j != row_len - 1:
            adj_rolls += is_roll(i-1, j+1)

        adj_rolls += is_roll(i-1, j)

    #same row
    if j != 0:
        adj_rolls += is_roll(i, j-1)

    if j != row_len - 1:
        adj_rolls += is_roll(i, j+1)

    #below
    if i != lines_len - 1:
        if j != 0:
            adj_rolls += is_roll(i+1, j-1)

        if j != row_len - 1:
            adj_rolls += is_roll(i+1, j+1)

        adj_rolls += is_roll(i+1, j)
    
    return adj_rolls


removed_rolls = 0
roll = "@"
roll_to_remove = "x"
empty = "."
filepath = "input.txt"
file = open(filepath)

lines = file.readlines()
lines = list(map(str.strip, lines))
lines = list(map(list, lines))
lines_len = len(lines)

while True:
    prev_removed_rolls = removed_rolls
    for i in range(lines_len):
        row_len = len(lines[i])
        for j in range(row_len):
            if lines[i][j] != roll:
                continue

            adj_rolls = get_adj_roll_count(i, j, lines_len, row_len)
            
            if adj_rolls < 4:
                lines[i][j] = roll_to_remove
                removed_rolls += 1
    
    for i in range(lines_len):
        for j in range(len(lines[i])):
            if lines[i][j] == roll_to_remove:
                lines[i][j] = empty
    
    if removed_rolls == prev_removed_rolls:
        break

print(removed_rolls)
