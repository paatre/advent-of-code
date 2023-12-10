import math
import re
from collections import defaultdict

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
categories = defaultdict(list)
category_index = 0

for line in lines[3:]:
    if not line:
        continue
    i = category_index
    if ":" in line:
        category_index += 1
        continue
    categories[i].append(list(map(int, line.split(" "))))

lowest_location_number = math.inf

for seed in seeds:
    current = seed
    for i in categories:
        for mapping in categories[i]:
            if mapping[1] <= current < mapping[1] + mapping[2]:
                current = mapping[0] + (current - mapping[1])
                break

    if current < lowest_location_number:
        lowest_location_number = current

print(lowest_location_number)
