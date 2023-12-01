import re

PATTERN = re.compile(r"([^0-9]+) ([0-9,]+) through ([0-9,]+)")

with open("06_input", "r") as file_input:
    light_grid = []
    for r in range(1000):
        light_grid.append([False for c in range(1000)])

    for line in file_input:
        match = PATTERN.match(line.strip())
        if match is not None:
            instruction = match.group(1)
            x_start, y_start = match.group(2).split(',')
            x_end, y_end = match.group(3).split(',')

            for x in range(int(x_start), int(x_end)+1):
                for y in range(int(y_start), int(y_end)+1):

                    if instruction == "turn on":
                        light_grid[x][y] = True

                    if instruction == "turn off":
                        light_grid[x][y] = False

                    if instruction == "toggle":
                        light_grid[x][y] = not light_grid[x][y]

    light_on_counter = 0
    for row in light_grid:
        for light in row:
            if light:
                light_on_counter += 1

    print(f"Part 1 - Light on {light_on_counter}")
