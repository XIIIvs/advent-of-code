class SourceToDestinationRange:
    def __init__(self, source_start, destination_start, range_length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.range_length = range_length

    def __repr__(self):
        return f"RangeMap <{self.source_start}-{self.source_start+self.range_length-1}> -> <{self.destination_start}-{self.destination_start+self.range_length-1}>"

    def return_destination_id(self, source_id: int):
        if self.source_start <= source_id < self.source_start + self.range_length:
            difference = source_id - self.source_start
            return self.destination_start + difference
        return None


class Map:
    def __init__(self):
        self.ranges = list()

    def add_range(self, range: SourceToDestinationRange):
        self.ranges.append(range)

    def return_destination_id(self, source_id: int):
        for source_destination_range in self.ranges:
            destination_id = source_destination_range.return_destination_ranges(source_id)
            if destination_id is not None:
                return destination_id
        return source_id


seeds = list()

maps = {
    "seed-to-soil": Map(),
    "soil-to-fertilizer": Map(),
    "fertilizer-to-water": Map(),
    "water-to-light": Map(),
    "light-to-temperature": Map(),
    "temperature-to-humidity": Map(),
    "humidity-to-location": Map(),
}

modes = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
    ""
]

with open("05_input", "r") as file_input:
    current_mode = None
    for line in file_input:
        to_parse = line.strip()

        if to_parse.startswith("seeds"):
            seeds = list(map(lambda x: int(x) if x.isnumeric() else None, to_parse.split(":")[1].strip().split(" ")))
        elif to_parse in modes:
            current_mode = to_parse[:-5]
            if to_parse == "":
                current_mode = None
        elif current_mode is not None:
            data = tuple(map(lambda x: int(x) if x.isnumeric() else None, to_parse.split(" ")))
            destination_range_start, source_range_start, range_length = data
            maps[current_mode].add_range(SourceToDestinationRange(source_range_start, destination_range_start, range_length))

location_to_seed = dict()
for seed in seeds:
    soil = maps["seed-to-soil"].return_destination_id(seed)
    fertilizer = maps["soil-to-fertilizer"].return_destination_id(soil)
    water = maps["fertilizer-to-water"].return_destination_id(fertilizer)
    light = maps["water-to-light"].return_destination_id(water)
    temperature = maps["light-to-temperature"].return_destination_id(light)
    humidity = maps["temperature-to-humidity"].return_destination_id(temperature)
    location = maps["humidity-to-location"].return_destination_id(humidity)
    location_to_seed[location] = seed

print(f"Part 1 - lowest location ({min(location_to_seed)}) is for seed: {location_to_seed[min(location_to_seed)]}")
