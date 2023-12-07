class Data:
    def __init__(self, time):
        self.time = time
        self.distance = None
        self.distance_to_speed = dict()
        self.ways_to_beat_the_record = 0

    def __repr__(self):
        return f"Data <{self.time} : {self.distance}> WIN ({self.ways_to_beat_the_record})"


with open("06_input", "r") as file_input:
    data_list = list()
    data_index = 0
    for line in file_input:
        current, data = line.strip().split(":")
        if current == "Time":
            for d in data.split(" "):
                if d == "":
                    continue
                if d.isnumeric():
                    data_list.append(Data(int(d)))
        elif current == "Distance":
            for d in data.split(" "):
                if d == "":
                    continue
                if d.isnumeric():
                    data_list[data_index].distance = int(d)
                    data_index += 1

multiplied_values = 1
for data in data_list:
    # charge_time == speed mm/s
    for charge_time in range(data.time+1):
        movement_time = data.time - charge_time
        distance = movement_time * charge_time
        if distance not in data.distance_to_speed:
            data.distance_to_speed[distance] = [charge_time]
        else:
            data.distance_to_speed[distance].append(charge_time)

    for distance in data.distance_to_speed:
        if distance > data.distance:
            data.ways_to_beat_the_record += len(data.distance_to_speed[distance])

    multiplied_values *= data.ways_to_beat_the_record

print(f"Part 1 - multiplied values: {multiplied_values}")
