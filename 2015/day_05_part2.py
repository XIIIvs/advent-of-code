NAUGHTY_SUBSTRINGS = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"

COUNTER = 0
with open("05_input", "r") as file_input:
    nice_string_counter = 0
    for line in file_input:
        COUNTER += 1
        string_to_check = line.strip()

        first_condition = False  # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps)
        second_condition = False  # It contains at least one letter which repeats with exactly one letter between them, like `xyx`, abcdefeghi (`efe`), or even `aaa`

        before_last_character = None
        last_character = None
        substrings = dict()
        seq_counter = 0
        for character in string_to_check:
            seq_counter += 1

            if before_last_character == character:
                second_condition = True

            if last_character is not None:
                substring = f"{last_character}{character}"
                if substring not in substrings:
                    substrings[substring] = [seq_counter-1, seq_counter]
                else:
                    if seq_counter-1 not in substrings[substring]:
                        first_condition = True

            before_last_character = last_character
            last_character = character

        if first_condition and second_condition:
            nice_string_counter += 1

    print(f"There are {nice_string_counter} nice strings")
