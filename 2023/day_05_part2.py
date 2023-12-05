from typing import List, Tuple


class SourceRange:
    def __init__(self, start, length):
        self.start = start
        self.end = start + length - 1
        self.length = length

    def __repr__(self):
        return f"Range <{self.start}-{self.end}>({self.length})"

    def __hash__(self):
        return hash((self.start, self.end, self.length))

    def __eq__(self, other):
        if isinstance(other, SourceRange):
            return self.start == other.start and self.end == other.end and self.length == other.length
        return False

    def remove_range(self, range_to_remove: "SourceRange") -> List["SourceRange"]:
        if range_to_remove is None:
            return [SourceRange(self.start, self.length)]
        elif range_to_remove.start <= self.start:
            if range_to_remove.end < self.end:
                return [SourceRange(range_to_remove.end + 1, self.end - range_to_remove.end)]
        elif self.start < range_to_remove.start <= self.end:
            if range_to_remove.end < self.end:
                return [
                    SourceRange(self.start, range_to_remove.start - self.start),
                    SourceRange(range_to_remove.end + 1, self.end - range_to_remove.end)
                ]
            else:
                return [SourceRange(self.start, range_to_remove.start - self.start)]
        elif self.end < range_to_remove.start:
            return [SourceRange(self.start, self.length)]
        return []


class SourceToDestinationRange:
    def __init__(self, source_start, destination_start, range_length):
        self.source_start = source_start
        self.source_end = source_start + range_length - 1
        self.destination_start = destination_start
        self.destination_end = destination_start + range_length - 1
        self.range_length = range_length

    def __repr__(self):
        return f"RangeMap <{self.source_start}-{self.source_start+self.source_end}> -> <{self.destination_start}-{self.destination_start+self.destination_end}>({self.range_length})"

    def return_destination_ranges(self, source_ranges: SourceRange) -> Tuple[SourceRange, SourceRange]:
        if source_ranges is None:
            return None, None
        elif source_ranges.start < self.source_start:
            if source_ranges.end < self.source_end:
                difference = source_ranges.end - self.source_start + 1
            else:
                difference = self.source_end - self.source_start + 1
            if difference > 0:
                return SourceRange(self.destination_start, difference), SourceRange(self.source_start, difference)
        elif self.source_start <= source_ranges.start <= self.source_end:
            delta = source_ranges.start - self.source_start
            destination_start = self.destination_start + delta
            if source_ranges.end < self.source_end:
                difference = source_ranges.end - source_ranges.start + 1
            else:
                difference = self.source_end - source_ranges.start + 1
            return SourceRange(destination_start, difference), SourceRange(source_ranges.start, difference)
        return None, None


class Map:
    def __init__(self):
        self.range_maps: List[SourceToDestinationRange] = list()

    def add_range(self, range_map: SourceToDestinationRange):
        self.range_maps.append(range_map)

    def return_destination_ranges(self, source_ranges: List[SourceRange]):
        destination_ranges = list()
        for source_range in source_ranges:
            tmp_source_range_list = [source_range]

            for range_map in self.range_maps:
                new_tmp_source_range_list = []
                if not tmp_source_range_list:
                    break
                for tmp_source_range in tmp_source_range_list:
                    destination_range, used_source_range = range_map.return_destination_ranges(tmp_source_range)
                    if destination_range is not None:
                        destination_ranges.append(destination_range)
                    new_tmp_source_range_list += tmp_source_range.remove_range(used_source_range)
                tmp_source_range_list = new_tmp_source_range_list.copy()

            if tmp_source_range_list:
                destination_ranges += tmp_source_range_list
        return destination_ranges


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

if __name__ == '__main__':
    with open("05_input", "r") as file_input:
        current_mode = None
        for line in file_input:
            to_parse = line.strip()

            if to_parse.startswith("seeds"):
                seed_range = list(map(lambda x: int(x) if x.isnumeric() else None, to_parse.split(":")[1].strip().split(" ")))
                for i in range(int(len(seed_range) / 2)):
                    start_range = seed_range[2 * i]
                    range_length = seed_range[2 * i + 1]
                    seeds.append(SourceRange(start_range, range_length))

            elif to_parse in modes:
                current_mode = to_parse[:-5]
                if to_parse == "":
                    current_mode = None
            elif current_mode is not None:
                data = tuple(map(lambda x: int(x) if x.isnumeric() else None, to_parse.split(" ")))
                destination_range_start, source_range_start, range_length = data
                maps[current_mode].add_range(SourceToDestinationRange(source_range_start, destination_range_start, range_length))

    location_ranges = set()
    for seed in seeds:
        soil = maps["seed-to-soil"].return_destination_ranges([seed])
        fertilizer = maps["soil-to-fertilizer"].return_destination_ranges(soil)
        water = maps["fertilizer-to-water"].return_destination_ranges(fertilizer)
        light = maps["water-to-light"].return_destination_ranges(water)
        temperature = maps["light-to-temperature"].return_destination_ranges(light)
        humidity = maps["temperature-to-humidity"].return_destination_ranges(temperature)
        location = maps["humidity-to-location"].return_destination_ranges(humidity)
        location_ranges.update(location)

    print(f"Part 2 - lowest location ({min(location_ranges, key=lambda x: x.start)})")
