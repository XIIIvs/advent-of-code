class Data:
    def __init__(self, time):
        self.time = time
        self.distance = None
        self.ways_to_beat_the_record = 0

    def __repr__(self):
        return f"Data <{self.time} : {self.distance}> WIN ({self.ways_to_beat_the_record})"


with open("06_input", "r") as file_input:
    for line in file_input:
        current, data_string = line.strip().split(":")
        if current == "Time":
            data = Data(int(data_string.replace(" ", "").strip()))
        elif current == "Distance":
            data.distance = int(data_string.replace(" ", "").strip())

#
charge_time = 0
movement_time = data.time
while charge_time <= movement_time:
    distance = charge_time * movement_time
    if distance > data.distance:
        break
    charge_time += 1
    movement_time -= 1

data.ways_to_beat_the_record = 1 + movement_time - charge_time

print(f"Part 2 - Nuber of ways to win race: {data.ways_to_beat_the_record}")
