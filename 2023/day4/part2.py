import re
from collections import defaultdict

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    amount_of_original_cards = len(lines)
    scratchcards = defaultdict(lambda: 1)

    for line_index, line in enumerate(lines):
        if line:
            card_parts = re.split(":\s|\s\|\s", line)
            pattern = "(?<=\d) "
            winning_numbers = set(map(int, re.split(pattern, card_parts[1])))
            my_numbers = set(map(int, re.split(pattern, card_parts[2])))
            matches = len(winning_numbers.intersection(my_numbers))
            for match in range(1, matches + 1):
                if line_index + match < amount_of_original_cards:
                    scratchcards[line_index + match] += scratchcards[line_index]

    print(sum(scratchcards[i] for i in range(amount_of_original_cards)))
