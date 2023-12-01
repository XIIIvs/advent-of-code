with open("03_input", "r") as file_input:
    for line in file_input:
        world_map = dict()
        current_position = 0, 0
        santa_position = 0, 0
        robot_position = 0, 0
        world_map[current_position] = 1
        step_counter = 0
        for direction in line:
            step_counter += 1
            if step_counter % 2 == 1:
                current_position = santa_position
            else:
                current_position = robot_position

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
            if step_counter % 2 == 1:
                santa_position = current_position
            else:
                robot_position = current_position

            if current_position not in world_map:
                world_map[current_position] = 1
            else:
                world_map[current_position] += 1

    print(f"Part 2 - number of houses {len(world_map)}")
