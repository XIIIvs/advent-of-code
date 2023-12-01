with open("03_input", "r") as file_input:
    for line in file_input:
        world_map = dict()
        current_position = 0, 0
        world_map[current_position] = 1
        for direction in line:
            x, y = current_position
            if direction == '<':
                x -= 1
            if direction == '>':
                x += 1
            if direction == '^':
                y += 1
            if direction == 'v':
                y -= 1

            current_position = x, y
            if current_position not in world_map:
                world_map[current_position] = 1
            else:
                world_map[current_position] += 1

    print(f"Part 1 - number of houses {len(world_map)}")
