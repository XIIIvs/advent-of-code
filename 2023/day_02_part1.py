import re

ID_PATTERN = re.compile(r"Game ([0-9]+): ")

with open("02_input", "r") as file_input:
    sum_of_ids = 0
    for line in file_input:
        to_parse = line.strip()

        match = ID_PATTERN.match(to_parse)
        if match is not None:
            game_id = int(match.group(1))
        else:
            print("Pattern not match")

        cubes = {
            "red": list(),
            "green": list(),
            "blue": list(),
        }
        records = to_parse.split(":")[1].strip().split(";")
        for record in records:
            for cube in record.split(", "):
                if cube.endswith(" red"):
                    cubes["red"].append(int(cube[:-4]))
                elif cube.endswith(" green"):
                    cubes["green"].append(int(cube[:-6]))
                elif cube.endswith(" blue"):
                    cubes["blue"].append(int(cube[:-5]))

        game_is_possible = max(cubes["red"]) <= 12 and max(cubes["green"]) <= 13 and max(cubes["blue"]) <= 14
        if game_is_possible:
            sum_of_ids += game_id

print(f"Part 1 - Sum of the IDs of impossible games = {sum_of_ids}")
