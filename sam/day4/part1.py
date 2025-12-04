def is_roll(line_i, char_i):
    return 1 if lines[line_i][char_i] == roll else 0

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

accessible_rolls = 0
roll = "@"
filepath = "input.txt"
file = open(filepath)

lines = file.readlines()
lines = list(map(str.strip, lines))
lines_len = len(lines)

for i in range(lines_len):
    row_len = len(lines[i])
    for j in range(row_len):
        adj_rolls = 0
        if lines[i][j] != roll:
            continue

        adj_rolls = get_adj_roll_count(i, j, lines_len, row_len)
        
        if adj_rolls < 4:
            accessible_rolls += 1

print(accessible_rolls)
