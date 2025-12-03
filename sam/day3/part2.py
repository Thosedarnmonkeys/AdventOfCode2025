def setIfBetterStartingAt(start: int, num: int, nums: list[int]):
    for j in range(start, 12):
        if nums[j] < num:
            nums[j] = num
            for k in range(j + 1, 12):
                nums[k] = 0
            break

total = 0
filepath = "input.txt"

file = open(filepath)
for line in file:
    nums = [0] * 12
    line = line.strip()
    twelfth_final_index = len(line) - 12
    indecies = range(len(line))

    for i in indecies:
        num = int(line[i])
        
        if i > twelfth_final_index:
            skip = i - twelfth_final_index
            setIfBetterStartingAt(skip, num, nums)

        else:
            setIfBetterStartingAt(0, num, nums)

    total += int(''.join(map(str, nums)))

print(total)