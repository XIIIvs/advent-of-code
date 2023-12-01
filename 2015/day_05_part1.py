NAUGHTY_SUBSTRINGS = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"

COUNTER = 0
with open("05_input", "r") as file_input:
    nice_string_counter = 0
    for line in file_input:
        COUNTER += 1
        string_to_check = line.strip()

        is_naughty = False
        for naughty_substring in NAUGHTY_SUBSTRINGS:
            if naughty_substring in string_to_check:
                is_naughty = True
                break
        if is_naughty:
            continue

        is_nice = False
        vowel_counter = 0
        last_character = None
        for character in string_to_check:
            if character == last_character:
                is_nice = True
            else:
                last_character = character
            if character in VOWELS:
                vowel_counter += 1

        if vowel_counter < 3:
            continue

        if is_nice:
            nice_string_counter += 1

    print(f"There are {nice_string_counter} nice strings")
