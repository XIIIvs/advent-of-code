puzzle_input = 368078
# puzzle_input = 30


def easy_read(number, place=2):
    string = str(number)
    if len(string) < place:
        num_of_spaces = place - len(string)
        string = num_of_spaces * " " + string
    return string
# for easy read in terminal


def change_position(position, xdir, ydir):
    new_x = position[0] + xdir
    new_y = position[1] + ydir
    return new_x, new_y

rng = range(puzzle_input+1)

rows = dict()
rows[0] = dict()
# rows[0][0] = easy_read(1)
rows[0][0] = 1

row_min = 0
row_max = 0

col_min = 0
col_max = 0

ydir = -1
xdir = 1
dir = 1

position = (0, 0)

for nr in rng[2:]:
    # value = easy_read(nr)
    value = 0

    if dir > 0:
        position = change_position(position, xdir, 0)
    else:
        position = change_position(position, 0, ydir)

    x = position[0]
    y = position[1]

    if y - 1 in rows:
        if x in rows[y - 1]:
            value += rows[y - 1][x]
        if x - 1 in rows[y - 1]:
            value += rows[y - 1][x - 1]
        if x + 1 in rows[y - 1]:
            value += rows[y - 1][x + 1]

    if y in rows:
        if x - 1 in rows[y]:
            value += rows[y][x - 1]
        if x + 1 in rows[y]:
            value += rows[y][x + 1]

    if y + 1 in rows:
        if x in rows[y + 1]:
            value += rows[y + 1][x]
        if x - 1 in rows[y + 1]:
            value += rows[y + 1][x - 1]
        if x + 1 in rows[y + 1]:
            value += rows[y + 1][x + 1]

    if y not in rows:
        rows[y] = dict()
    rows[y][x] = value

    print("for number", easy_read(nr), "is >", easy_read(value, 6), "<")
    if value > puzzle_input:
        break

    if dir > 0:
        if xdir > 0:
            if not x > col_max:
                continue
            else:
                dir = -1
                xdir = -1
                col_max += 1
        else:
            if not x < col_min:
                continue
            else:
                dir = -1
                xdir = 1
                col_min -= 1
    else:
        if ydir > 0:
            if not y > row_max:
                continue
            else:
                dir = 1
                ydir = -1
                row_max += 1
        else:
            if not y < row_min:
                continue
            else:
                dir = 1
                ydir = 1
                row_min -= 1