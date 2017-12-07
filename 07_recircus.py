with open("input_07.txt") as file:

    words = dict()

    for line in file:
        word = line[:-1]
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    for key in sorted(words):
        if words[key] == 1:
            print("IT IS HERE FUCKA [", key, "]")
        # else:
        #     print(key)
