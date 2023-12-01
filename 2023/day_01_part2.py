def is_string(string, index, expected_string, value):
    string_length = len(string)
    expected_string_length = len(expected_string)
    end_index = index + expected_string_length
    if end_index <= string_length:
        if string[index:end_index] == expected_string:
            return value
    return None


string_to_digit = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]

with open("01_input", "r") as file_input:
    sum_of_digits = 0
    for line in file_input:
        to_parse = line.strip()

        new_string = ""
        iterator = 0
        to_parse_length = len(to_parse)
        while iterator != to_parse_length:
            char = to_parse[iterator]
            values = set(map(lambda x: is_string(to_parse, iterator, x[0], x[1]), string_to_digit))
            values.remove(None)
            if len(values) != 0:
                new_string += values.pop()
            new_string += char
            iterator += 1

        digit = ""
        for char in new_string:
            if char.isnumeric():
                digit += char
                break
        for char in reversed(new_string):
            if char.isnumeric():
                digit += char
                break
        sum_of_digits += int(digit)
        pass

print(f"Part 2 - sum of digits: {sum_of_digits}")
