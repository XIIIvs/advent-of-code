import re


def easy_read(number, place=2):
    string = str(number)
    if len(string) < place:
        num_of_spaces = place - len(string)
        string = num_of_spaces * " " + string
    return string
# for easy read in terminal

blocks = dict()

def do_operation(name, op, value):
    before = blocks[name]
    if op == "dec":
        blocks[name] -= value
    if op == "inc":
        blocks[name] += value
    print(" - DO:", name, op, value, "before:", before, "now:", blocks[name])

with open("input_08.txt") as file:
    for line in file:
        match = re.match(r"([a-z]+) ([cdein]+) ([0-9-]+) if ([a-z]+) ([-=><!]+) ([0-9-]+)", line)
        if match:
            block_name = match.group(1)
            operation = match.group(2)  # dec or inc
            op_value = int(match.group(3))
            cnd_name = match.group(4)
            comparator = match.group(5)  # == < > <= >= !=
            cp_value = int(match.group(6))

            if block_name not in blocks:
                blocks[block_name] = 0
            if cnd_name not in blocks:
                blocks[cnd_name] = 0

            if comparator == "==" and blocks[cnd_name] == cp_value:
                do_operation(block_name, operation, op_value)
            elif comparator == "<" and blocks[cnd_name] < cp_value:
                do_operation(block_name, operation, op_value)
            elif comparator == ">" and blocks[cnd_name] > cp_value:
                do_operation(block_name, operation, op_value)
            elif comparator == "<=" and blocks[cnd_name] <= cp_value:
                do_operation(block_name, operation, op_value)
            elif comparator == ">=" and blocks[cnd_name] >= cp_value:
                do_operation(block_name, operation, op_value)
            elif comparator == "!=" and blocks[cnd_name] != cp_value:
                do_operation(block_name, operation, op_value)
            else:
                print(cnd_name, "(" + str(blocks[cnd_name]) + ")", "is not", comparator, cp_value)

answers = list()
for key in blocks:
    ans = (blocks[key], key)
    answers.append(ans)

for a in sorted(answers):
    print(a)