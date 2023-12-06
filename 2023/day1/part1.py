import re

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    sum_of_calibration_values = 0
    for line in lines:
        if line:
            first = re.findall("\d", line)[0]
            last = re.findall("\d", line)[-1]
            sum_of_calibration_values += int(first + last)
            print(sum_of_calibration_values)
    print(sum_of_calibration_values)
