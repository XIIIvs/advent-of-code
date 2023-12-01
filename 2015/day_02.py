with open("02_input", "r") as file_input:
    paper_needed = 0
    ribbon_needed = 0
    for line in file_input:
        l, w, h = tuple(map(lambda i: int(i), line.strip().split("x")))

        # part 1
        side_lw = l * w
        side_lh = l * h
        side_wh = w * h
        extra_side = min(side_lw, side_lh, side_wh)
        paper_for_present = 2 * side_lw + 2 * side_lh + 2 * side_wh + extra_side
        paper_needed += paper_for_present

        # part 2
        shortest_side, medium_side, longest_side = tuple(sorted([l, w, h]))
        ribbon_wrap = 2 * shortest_side + 2 * medium_side
        ribbon_bow = l * w * h
        ribbon_for_present = ribbon_wrap + ribbon_bow
        ribbon_needed += ribbon_for_present

    print(f"Part 1 - Paper needed: {paper_needed}")
    print(f"Part 2 - Ribbon needed: {ribbon_needed}")
