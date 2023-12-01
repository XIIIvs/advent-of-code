with open("01_input", "r") as file_input:
    sum_of_digits = 0
    for line in file_input:
        to_parse = line.strip()

        digit = ""
        for char in to_parse:
            if char.isnumeric():
                digit += char
                break
        for char in reversed(to_parse):
            if char.isnumeric():
                digit += char
                break
        sum_of_digits += int(digit)

print(f"Part 1 - sum of digits: {sum_of_digits}")
