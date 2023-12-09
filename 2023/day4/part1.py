import re
from functools import reduce

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    points = 0

    for line in lines:
        if line:
            card_parts = re.split(":\s|\s\|\s", line)
            pattern = "(?<=\d) "
            winning_numbers = set(map(int, re.split(pattern, card_parts[1])))
            my_numbers = set(map(int, re.split(pattern, card_parts[2])))
            same_numbers = winning_numbers.intersection(my_numbers)
            points += reduce(lambda a, b: 1 if a == 0 else a * 2, same_numbers, 0)

    print(points)
