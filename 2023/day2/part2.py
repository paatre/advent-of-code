import re
from collections import defaultdict
from functools import reduce

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    sum_of_powers = 0

    for line in lines:
        if line:
            game = line[line.index(':') + 2:]
            results = re.findall("(\d+ (?:red|green|blue))", game)
            min_by_color = defaultdict(int)
            for result in results:
                count, color = result.split(' ')
                if int(count) > min_by_color[color]: min_by_color[color] = int(count)
            power = reduce(lambda a, b: a * b, min_by_color.values())
            sum_of_powers += power
    print(sum_of_powers)
