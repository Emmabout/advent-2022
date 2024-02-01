
def get_minmax(range1, range2):
    min1, max1 = range1.split('-')
    min2, max2 = range2.split('-')
    min1 = int(min1)
    max1 = int(max1)
    min2 = int(min2)
    max2 = int(max2)
    return min1, max1, min2, max2

def is_fully_contained(range1, range2):
    min1, max1, min2, max2 = get_minmax(range1, range2)
    if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
        return 1
    return 0

def part1():
    with open("advent4_input.txt", "r") as f: #advent4_input
        fully_contained_pairs = 0
        for line in f.read().splitlines():
            range1, range2 = line.split(',')
            is_contained = is_fully_contained(range1, range2)
            fully_contained_pairs += is_contained
        print("Sum:", fully_contained_pairs)

def does_ranges_overlap(range1, range2):
    min1, max1, min2, max2 = get_minmax(range1, range2)
    return (min1<=max2 and min1 >=min2) or (max1<=max2 and max1>=min2) or (min2<=max1 and min2 >=min1) or (max2<=max1 and max2>=min1)


def part2():
    with open("advent4_input.txt", "r") as f: #advent4_input
        overlapping_pairs = 0
        for line in f.read().splitlines():
            range1, range2 = line.split(',')
            are_overlapping = does_ranges_overlap(range1, range2)
            overlapping_pairs += are_overlapping
        print(overlapping_pairs)

def main():
    print("Part 1")
    part1()
    print("Part 2")
    part2()
    return 0




if __name__ == "__main__":
    main()