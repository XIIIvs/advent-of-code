with open("02_input", "r") as file_input:
    sum_of_power = 0
    for line in file_input:
        to_parse = line.strip()

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

        power = max(cubes["red"]) * max(cubes["green"]) * max(cubes["blue"])
        sum_of_power += power

print(f"Part 2 - Sum of the power = {sum_of_power}")
