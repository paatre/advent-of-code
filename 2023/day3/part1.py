import re
from collections import defaultdict, deque

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    line_length = len(lines[0])
    sum_of_part_numbers = 0
    numbers = defaultdict(list)
    symbols = defaultdict(list)

    for line_index, line in enumerate(lines):
        if line:
            matches = re.finditer("\d+|[^.\d]", line)
            for match in matches:
                index = match.start()
                group = match.group()
                if group.isdigit():
                    numbers[line_index].append((group, index))
                else:
                    symbols[line_index].append(index)

    for line, numbers_indexes in numbers.items():
        for number, index in numbers_indexes:
            left = index - 1 if index > 0 else None
            middle = list(range(index, index + len(number)))
            right = index + len(number) if index + len(number) <= line_length else None
            indexes_to_check = deque(middle)
            if left:
                indexes_to_check.appendleft(left)
            if right:
                indexes_to_check.append(right)
            indexes_to_check = set(indexes_to_check)
            above = set(symbols[line - 1]) & indexes_to_check if line > 0 else False 
            same = set(symbols[line]) & indexes_to_check
            below = set(symbols[line + 1]) & indexes_to_check if line < len(lines) - 1 else False
            if above or same or below:
                sum_of_part_numbers += int(number)

    print(sum_of_part_numbers)
