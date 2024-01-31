
def find_common_item(comp1, comp2):
    for item1 in comp1:
        for item2 in comp2:
            if item1 == item2:
                return item1

def find_priority(char):
    if(char.isupper()):
        return ord(char) - 38
    return ord(char) - 96

def part1():
    with open("advent3_input.txt", "r") as f: #advent3_input
        prio_sum = 0
        for line in f.read().splitlines():
            comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
            common_item = find_common_item(comp1, comp2)
            prio = find_priority(common_item)
            prio_sum += prio
        print(prio_sum)

def find_common_item3(comp1, comp2, comp3):
    list_commons = []
    for item1 in comp1:
        for item2 in comp2:
            if item1 == item2:
                list_commons.append(item1)
    for item in list_commons:
        for item3 in comp3:
            if item == item3:
                return item
            
def part2():
    with open("advent3_input.txt", "r") as f: #advent3_input
        prio_sum = 0
        all_lines = f.read().splitlines()
        for i in range(len(all_lines)//3):
            common_item = find_common_item3(all_lines[3*i], all_lines[3*i+1], all_lines[3*i+2])
            prio = find_priority(common_item)
            prio_sum += prio
        print(prio_sum)

def main():
    print("Part 1")
    part1()
    print("Part 2")
    part2()
    return 0




if __name__ == "__main__":
    main()