import re

ID_PATTERN = re.compile(r"Card +([0-9]+)")

with open("04_input", "r") as file_input:
    cards_dict = dict()
    for line in file_input:
        card_lp_string, number_sets_string = line.strip().split(":")
        winning_number_set_string, selected_number_set_string = number_sets_string.split("|")

        winning_number_set = set(map(lambda x: int(x) if x.isnumeric() else None, winning_number_set_string.split(" ")))
        winning_number_set.remove(None)

        selected_number_set = set(map(lambda x: int(x) if x.isnumeric() else None, selected_number_set_string.split(" ")))
        selected_number_set.remove(None)

        card_id = None
        match = ID_PATTERN.match(card_lp_string)
        if match is not None:
            card_id = int(match.group(1))
        if card_id not in cards_dict:
            cards_dict[card_id] = 1  # add original

        current_winning_card = card_id
        for selected_number in selected_number_set:
            if selected_number in winning_number_set:
                current_winning_card += 1
                if current_winning_card not in cards_dict:
                    cards_dict[current_winning_card] = 1  # add original
                cards_dict[current_winning_card] += cards_dict[card_id]  # add copies

    sum_of_cards = 0
    for card_id, amount in cards_dict.items():
        sum_of_cards += amount

print(f"Part 2 - Sum of the cards: {sum_of_cards}")
