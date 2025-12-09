class FreshIngredientRange:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def is_in_range(self, id: int):
        return id >= self.min and id <= self.max

    def size(self):
        return self.max - self.min + 1

def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def read_input_into_fresh_and_available_ingredients(file_path) -> tuple[list[FreshIngredientRange], list[int]]:
    fresh_ingredient_ranges = []
    available_ingredients = []

    for line in read_input(file_path):
        if len(line) == 0:
            continue

        parts = line.split('-')
        if len(parts) == 2:
            fresh_ingredient_ranges.append(FreshIngredientRange(int(parts[0]), int(parts[1])))
        else:
            available_ingredients.append(int(line))

    return fresh_ingredient_ranges, available_ingredients

def main():
    new_ranges = []

    fresh_ingredient_ranges, _ = read_input_into_fresh_and_available_ingredients("input.txt")
    fresh_ingredient_ranges.sort(key=lambda range: range.min)

    new_ranges.append(fresh_ingredient_ranges[0])
    i = 1
    while i < len(fresh_ingredient_ranges):
        previous_range = new_ranges[-1]
        current_range = fresh_ingredient_ranges[i]

        if current_range.min > previous_range.max:
            new_ranges.append(current_range)
        elif current_range.min == previous_range.max:
            new_ranges.append(FreshIngredientRange(current_range.min + 1, current_range.max))
        else:
            if current_range.max > previous_range.max:
                new_ranges.append(FreshIngredientRange(previous_range.max + 1, current_range.max))

        i += 1

    print(f"The total number of fresh ingredients is: {sum(range.size() for range in new_ranges)}")

if __name__ == "__main__":
    main()