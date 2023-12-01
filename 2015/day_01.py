with open("01_input", "r") as file_input:
    for line in file_input:
        current_floor = 0
        instruction_counter = 0
        for char in line:
            # part 1
            if char == "(":
                current_floor += 1
            if char == ")":
                current_floor -= 1

            # part 2
            if instruction_counter is not None:
                instruction_counter += 1
                if current_floor == -1:
                    print(f"Part 2 - Entered to basement on [{instruction_counter}] position")
                    instruction_counter = None

        print(f"Part 1 - Floor: {current_floor}")
