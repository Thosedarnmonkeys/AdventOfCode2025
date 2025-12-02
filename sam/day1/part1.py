zeros = 0
dial = 50
filepath = "input.txt"

file = open(filepath)
for line in file:
    direction = line[:1]
    value = int(line[1:])
    
    if direction == "L":
        value *= -1
    
    dial += value

    dial = dial % 100

    if dial == 0:
        zeros += 1

print(zeros)