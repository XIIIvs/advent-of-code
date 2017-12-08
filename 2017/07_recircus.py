import re
import copy

base_weight = dict()
cascade = dict()

with open("input_07.txt") as file:
    for line in file:
        match = re.match(r"([a-z]+) \(([0-9]+)\)", line[:-1])

        if match:
            key = match.group(1)
            base_weight[key] = int(match.group(2))

        cascade_match = re.match(r"([a-z]+) \([0-9]+\) -> (.*)", line[:-1])

        if cascade_match:
            key = cascade_match.group(1)
            cascade[key] = dict()
            for e in cascade_match.group(2).split(", "):
                cascade[key][e] = 0

in_cascade = set()
cascade_keys = set()
for key in sorted(cascade):
    cascade_keys.add(key)
    for element in sorted(cascade[key]):
        in_cascade.add(element)

resolved = dict()
weight = copy.deepcopy(base_weight)

while len(cascade_keys) > 0:
    print("cascade keys:", len(cascade_keys), "in cascade:", len(in_cascade))

    for ica in sorted(in_cascade):
        if ica in cascade_keys:
            continue
        else:
            resolved[ica] = weight[ica]
            in_cascade.remove(ica)

    for cke in sorted(cascade_keys):
        minimum = 999999
        for key in cascade[cke]:
            if key in resolved:
                cascade[cke][key] = resolved[key]
            if cascade[cke][key] < minimum:
                minimum = cascade[cke][key]
        if minimum > 0:
            cascade_keys.remove(cke)
            for key in cascade[cke]:
                weight[cke] += cascade[cke][key]


for key in sorted(base_weight):
    print(key, "->", base_weight[key], "(", weight[key], ")")
    if key in cascade:
        print(" -", cascade[key])
