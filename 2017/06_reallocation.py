banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

steps = int()
answers = list()
ans = tuple(banks)
print(ans, "steps =", steps)

indexes = len(banks)

while ans not in answers:
    answers.append(ans)
    steps += 1
    blocks = max(banks)
    index = banks.index(blocks)
    banks[index] = 0

    for blck in range(blocks):
        index += 1
        index %= indexes
        banks[index] += 1

    ans = tuple(banks)
    print(ans, "steps =", steps)

new_ans = int()
loop_cnt = int()

while new_ans != ans:
    loop_cnt += 1
    blocks = max(banks)
    index = banks.index(blocks)
    banks[index] = 0

    for blck in range(blocks):
        index += 1
        index %= indexes
        banks[index] += 1

    new_ans = tuple(banks)
    print(new_ans, "loop_cnt =", loop_cnt)
