import re
from collections import defaultdict, deque
from functools import reduce

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    line_length = len(lines[0])
    sum_of_gear_ratios = 0
    numbers = defaultdict(list)
    gears = defaultdict(list)

    for line_index, line in enumerate(lines):
        if line:
            matches = re.finditer("\d+|\*", line) 
            for match in matches: 
                index = match.start() 
                group = match.group() 
                if group.isdigit(): 
                    indexes = list(range(index, index + len(group))) 
                    numbers[line_index].append((group, indexes)) 
                else:
                    gears[line_index].append(index)

    for line, gear_indexes in gears.items():
        for gear_index in gear_indexes:
            left = gear_index - 1 if gear_index > 0 else None
            middle = [gear_index]
            right = gear_index + 1 if gear_index + 1 <= line_length else None
            indexes_to_check = deque(middle)
            if left:
                indexes_to_check.appendleft(left)
            if right:
                indexes_to_check.append(right)
            indexes_to_check = set(indexes_to_check)

            def indexes_for_numbers_by_line(number_line):
                return set([index for number_tuple in numbers[number_line] for index in number_tuple[1]])

            above = indexes_for_numbers_by_line(line - 1) & indexes_to_check
            same = indexes_for_numbers_by_line(line) & indexes_to_check
            below = indexes_for_numbers_by_line(line + 1) & indexes_to_check

            adjacent_indexes = above | same | below

            def numbers_for_numbers_by_line(number_line, indexes):
                adjacent_numbers = []
                number_tuples = [*numbers[number_line - 1], *numbers[number_line], *numbers[number_line + 1]]
                for number_tuple in number_tuples:
                    number, number_indexes = number_tuple
                    if adjacent_indexes & set(number_indexes):
                        adjacent_numbers.append(number)
                return adjacent_numbers

            adjacent_part_numbers = numbers_for_numbers_by_line(line, adjacent_indexes)
            sum_of_gear_ratios += reduce(lambda a, b: int(a) * int(b), adjacent_part_numbers, 1) if len(adjacent_part_numbers) > 1 else 0

    print(sum_of_gear_ratios)
