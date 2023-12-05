from day_05_part2 import SourceRange, SourceToDestinationRange

source_range_test_data = [
    (None, [SourceRange(10, 11)]),  # None -> 10-20
    (SourceRange(8, 2), [SourceRange(10, 11)]),  # 8-9 -> 10-20
    (SourceRange(8, 3), [SourceRange(11, 10)]),  # 8-10 -> 11-20
    (SourceRange(8, 8), [SourceRange(16, 5)]),  # 8-15 -> 16-20
    (SourceRange(8, 13), []),  # 8-20 -> empty
    (SourceRange(8, 18), []),  # 8-25 -> empty
    (SourceRange(10, 1), [SourceRange(11, 10)]),  # 10-10 -> 11-20
    (SourceRange(10, 6), [SourceRange(16, 5)]),  # 10-15 -> 16-20
    (SourceRange(10, 11), []),  # 10-20 -> empty
    (SourceRange(10, 16), []),  # 10-25 -> empty
    (SourceRange(15, 1), [SourceRange(10, 5), SourceRange(16, 5)]),  # 15-15 -> 10-14 and 16-20
    (SourceRange(15, 3), [SourceRange(10, 5), SourceRange(18, 3)]),  # 15-17 -> 10-14 and 18-20
    (SourceRange(15, 6), [SourceRange(10, 5)]),  # 15-20 -> 10-14
    (SourceRange(15, 11), [SourceRange(10, 5)]),  # 15-25 -> 10-14
    (SourceRange(20, 1), [SourceRange(10, 10)]),  # 20-20 -> 10-19
    (SourceRange(20, 6), [SourceRange(10, 10)]),  # 20-25 -> 10-19
    (SourceRange(22, 4), [SourceRange(10, 11)]),  # 22-25 -> 10-20
]

source_to_destination_range_test_data = [
    (None, (None, None)),  # None -> None, None
    (SourceRange(5, 4), (None, None)),  # 5-8 -> None, None
    (SourceRange(5, 6), (SourceRange(100, 1), SourceRange(10, 1))),  # 5-10 -> 100-100, 10-10
    (SourceRange(5, 11), (SourceRange(100, 6), SourceRange(10, 6))),  # 5-15 -> 100-105, 10-15
    (SourceRange(5, 16), (SourceRange(100, 11), SourceRange(10, 11))),  # 5-20 -> 100-110, 10-20
    (SourceRange(5, 21), (SourceRange(100, 11), SourceRange(10, 11))),  # 5-25 -> 100-110, 10-20
    (SourceRange(10, 1), (SourceRange(100, 1), SourceRange(10, 1))),  # 10-10 -> 100-100, 10-10
    (SourceRange(10, 6), (SourceRange(100, 6), SourceRange(10, 6))),  # 10-15 -> 100-105, 10-15
    (SourceRange(10, 11), (SourceRange(100, 11), SourceRange(10, 11))),  # 10-20 -> 100-110, 10-20
    (SourceRange(10, 16), (SourceRange(100, 11), SourceRange(10, 11))),  # 10-25 -> 100-110, 10-20
    (SourceRange(15, 1), (SourceRange(105, 1), SourceRange(15, 1))),  # 15-15 -> 105-105, 15-15
    (SourceRange(15, 4), (SourceRange(105, 4), SourceRange(15, 4))),  # 15-18 -> 105-108, 15-18
    (SourceRange(15, 6), (SourceRange(105, 6), SourceRange(15, 6))),  # 15-20 -> 105-110, 15-20
    (SourceRange(15, 11), (SourceRange(105, 6), SourceRange(15, 6))),  # 15-25 -> 105-110, 15-20
    (SourceRange(20, 1), (SourceRange(110, 1), SourceRange(20, 1))),  # 20-20 -> 110-110, 20-20
    (SourceRange(20, 6), (SourceRange(110, 1), SourceRange(20, 1))),  # 20-25 -> 110-110, 20-20
    (SourceRange(21, 5), (None, None)),  # 21-25 -> None, None
]

if __name__ == '__main__':
    given = SourceRange(10, 11)  # 10 - 20
    for to_remove_range, expected in source_range_test_data:
        actual = given.remove_range(to_remove_range)
        print(f"SourceRange Tests: {'' if actual==expected else 'TEST FAILED !!!!!!!!!! '}When from range {given} remove range {to_remove_range} = {actual} and should be {expected}")

    given = SourceToDestinationRange(10, 100, 11)  # 10-20 -> 100-110
    for source_range, expected in source_to_destination_range_test_data:
        actual = given.return_destination_ranges(source_range)
        print(f"SourceToDestination Tests: {'' if actual==expected else 'TEST FAILED !!!!!!!!!! '}When get destination for {source_range} = {actual} and should be {expected}")
