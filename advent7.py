
def init():
    with open("advent7_input.txt", "r") as f: #advent7_input
        data = f.read()
    return data

def get_files_below(parents, size):
    total = 0
    for parent in parents:
        if parents[parent]<=size:
            total += parents[parent]
    print(total) 

def find_min(parents):
    needed_space = 30000000 - (70000000 - parents['/'])
    print("needed space", needed_space)
    min_size = 30000000
    for name, size in parents.items():
        if(size) >= needed_space and size < min_size:
            min_size = size
    print("minimum size: ", min_size)

def part1and2():
    data = init()
    commands = data.splitlines()
    allparents = {}
    subparents = []
    for cmd in commands:
        print(cmd)
        if "cd .." not in cmd:
            if " cd " in cmd:
                parent = cmd.split(" cd ")[1]
                while parent in allparents:
                    parent = parent + "a"
                subparents.append(parent)
                allparents[parent] = 0
            elif "dir" not in cmd and "$ ls" not in cmd:
                for k in subparents:
                    allparents[k] += int(cmd.split(" ")[0])
        else:
            subparents.pop()
    print(allparents)
    find_min(allparents)
    get_files_below(allparents, 100000)

def main():
    part1and2()
    return 0


if __name__ == "__main__":
    main()