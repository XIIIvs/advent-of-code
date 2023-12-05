with open("04_input", "r") as file_input:
    sum_of_points = 0
    for line in file_input:
        card_lp_string, number_sets_string = line.strip().split(":")
        winning_number_set_string, selected_number_set_string = number_sets_string.split("|")

        winning_number_set = set(map(lambda x: int(x) if x.isnumeric() else None, winning_number_set_string.split(" ")))
        winning_number_set.remove(None)

        selected_number_set = set(map(lambda x: int(x) if x.isnumeric() else None, selected_number_set_string.split(" ")))
        selected_number_set.remove(None)

        points = None
        for selected_number in selected_number_set:
            if selected_number in winning_number_set:
                if points is not None:
                    points *= 2
                else:
                    points = 1
        if points is not None:
            sum_of_points += points

    print(f"Part 1 - Sum of the points: {sum_of_points}")
