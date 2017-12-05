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
rows[0][0] = easy_read(1)

row_min = 0
row_max = 0

col_min = 0
col_max = 0

ydir = -1
xdir = 1
dir = 1

position = (0, 0)

for nr in rng[2:]:
    value = easy_read(nr)

    if dir > 0:
        position = change_position(position, xdir, 0)
    else:
        position = change_position(position, 0, ydir)

    x = position[0]
    y = position[1]

    if y not in rows:
        rows[y] = dict()
    rows[y][x] = value

    print("for value", value, "number of steps is", abs(x) + abs(y), "( on position x =", x, "y =", y, ")")

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