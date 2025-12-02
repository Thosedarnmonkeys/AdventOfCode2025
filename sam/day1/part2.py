zeros = 0
dial = 50
filepath = "input.txt"

count = 0

file = open(filepath)
for line in file:
    direction = line[:1]
    value = int(line[1:])
    
    if direction == "L":
        value *= -1

    nextDial = dial + value

    if nextDial == 0:
        zeros += 1

    elif (nextDial < 0):
        zeros += int(nextDial / -100) + (1 if dial != 0 else 0)

    elif(nextDial > 99):
        zeros += int(nextDial / 100)

    dial = nextDial % 100

print(zeros)