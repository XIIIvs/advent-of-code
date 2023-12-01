import re

PATTERN = re.compile(r"(\\x[0-9a-f]{2})")

with open("08_input", "r") as file_input:
    sum_character_code_and_memory = 0
    for line in file_input:
        to_parse = line.strip()
        string_code_length = len(to_parse)
        sum_character_code_and_memory += string_code_length

        new_string = to_parse[1:-1]
        new_string = new_string.replace("\\\"", "\"")
        new_string = new_string.replace("\\\\", "\\")
        print(to_parse, "|", new_string)

print(f"Part 1 - Sum od code and in memory character lengths: {sum_character_code_and_memory}")
