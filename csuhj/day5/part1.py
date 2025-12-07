class FreshIngredientRange:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def is_in_range(self, id: int):
        return id >= self.min and id <= self.max

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
    number_of_fresh_ingredients = 0

    fresh_ingredient_ranges, available_ingredients = read_input_into_fresh_and_available_ingredients("input.txt")
    for id in available_ingredients:
        matching_ranges = list(filter(lambda range: range.is_in_range(id), fresh_ingredient_ranges))
        if len(matching_ranges) > 0:
            number_of_fresh_ingredients += 1
    
    print(f"The number of fresh ingredients is: {number_of_fresh_ingredients}")

if __name__ == "__main__":
    main()