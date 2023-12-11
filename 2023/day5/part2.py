import math
import re
from collections import defaultdict

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
seed_ranges = [range(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

categories = defaultdict(list)

for line in lines[3:]:
    if not line:
        continue
    category_index = 0
    if ":" in line:
        category_index  += 1
        continue
    categories[category_index].append(list(map(int, line.split(" "))))

lowest_location_number = math.inf

for seed_range in seed_ranges:
    for i in categories:
        # TODO: How to apply destination ranges to map handling?
        destination_ranges = []
        for destination_range_start, source_range_start, range_length in categories[i]:

            def is_inside_mapping_range(seed):
                return source_range_start <= seed < source_range_start + range_length

            # TODO: How to handle seed ranges larger than source ranges?

            # Current range starts inside mapping range
            if is_inside_mapping_range(seed_range.start):
                start = destination_range_start + (seed_range.start - source_range_start)
            else:
                start = seed_range.start

            # Current range ends inside mapping range
            if is_inside_mapping_range(seed_range.stop):
                stop = start + (seed_range.stop - seed_range.start)
            else:
                stop = seed_range.stop

            # Current range starts outside source range
            if start == seed_range.start:
                # Current range stops outside source range
                if stop == seed_range.stop:
                    # Return original range
                    r1 = range(start, stop)
                    destination_ranges.append(r1)
                # Current range stops inside source range
                else:
                    # Split current range at destination range start
                    r1 = range(start, destination_range_start)
                    r2 = range(destination_range_start, stop)
                    destination_ranges.append(r1, r2)
            # Current range starts inside source range
            else:
                # Current range stops outside source range
                if stop == seed_range.stop:
                    # Split range at destination range stop
                    r1 = range(start, destination_range_start + range_length)
                    r2 = range(destinaton_range_start + range_length, stop)
                    destination_ranges.append(r1, r2)
                # Current range stops inside source range
                else:
                    # Return mapped range
                    r1 = range(start, stop)
                    destination_ranges.append(r1)
            break

    if destination_range.start < lowest_location_number:
        lowest_location_number = current_range.start

print(lowest_location_number)
