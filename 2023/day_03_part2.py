class Symbol:
    def __init__(self, symbol: str, x: int, row: int):
        self.symbol = symbol
        self.x = x
        self.row = row

    def __repr__(self):
        return f"[{self.symbol}] <{self.x}, {self.row}>"


class Number:
    def __init__(self, start: int, end: int, row: int, value: int):
        self.start = start
        self.end = end
        self.row = row
        self.value = value

    def __repr__(self):
        return f"Number [{self.value}] at <({self.start}-{self.end}), {self.row}>"

    def __hash__(self):
        return hash((self.start, self.end, self.row))

    def touch_symbol(self, symbol: Symbol):
        return (self.start - 1) <= symbol.x < (self.end + 1) and self.row - 1 <= symbol.row <= self.row + 1


with open("03_input", "r") as file_input:
    number_set = set()
    symbol_list = list()

    row_number = 0
    for line in file_input:
        to_parse = line

        number_string = ""
        tmp_i = 0
        for i in range(len(to_parse)):
            char = line[i]
            if char.isnumeric():
                if number_string == "":
                    tmp_i = i
                number_string += char
            else:
                if number_string != "":
                    number_set.add(Number(tmp_i, i, row_number, int(number_string)))
                    number_string = ""
                if char not in (".", "\n"):
                    symbol_list.append(Symbol(char, i, row_number))
            i += 1
        row_number += 1

    sum_of_gear_ratios = 0
    for s in symbol_list:
        if s.symbol != "*":
            continue

        gear_number_set = set()
        for n in number_set:
            if len(gear_number_set) > 2:
                break
            if n.touch_symbol(s):
                gear_number_set.add(n)
        if len(gear_number_set) == 2:
            sum_of_gear_ratios += gear_number_set.pop().value * gear_number_set.pop().value


print(f"Part 2 - Sum of the gear ratios: {sum_of_gear_ratios}")
