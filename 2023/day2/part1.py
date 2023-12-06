import re

with open('input.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    sum_of_game_ids = 0
    re_max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def validate_game(results):
        for result in results:
            count, color = result.split(' ')
            if int(count) > re_max_cubes[color]:
                return False
        return True

    for line in lines:
        if line:
            game = line[line.index(':') + 2:]
            results = re.findall("(\d+ (?:red|green|blue))", game)
            game_is_valid = validate_game(results)
            if game_is_valid:
                game_id = re.findall("\d+", line)[0]
                sum_of_game_ids += int(game_id)
    print(sum_of_game_ids)
