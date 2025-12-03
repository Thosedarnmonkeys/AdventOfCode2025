total = 0
filepath = "input.txt"

file = open(filepath)
for line in file:
    num1, num2 = 0, 0
    line = line.strip()
    final_index = len(line) - 1
    indecies = range(len(line))

    for i in indecies:
        num = int(line[i])
        
        if i == final_index:
            if num2 < num:
                num2 = num

        elif num1 < num:
            num1 = num
            num2 = 0

        elif num2 < num:
            num2 = num


    total += int(str(num1) + str(num2))

print(total)