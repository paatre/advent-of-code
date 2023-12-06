import re

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    sum_of_calibration_values = 0
    allowed_values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '\d']
    string_to_int = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for row, line in enumerate(lines):
        if line:
            first = re.findall('|'.join(allowed_values), line)[0]
            first = string_to_int[first] if not first.isdigit() else first
            last = re.findall("(?=(" + "|".join(allowed_values) + "))", line)[-1]
            last = string_to_int[last] if not last.isdigit() else last
            calibration_value = int(first + last)
            sum_of_calibration_values += calibration_value
    print(sum_of_calibration_values)
