
import numpy as np

def init():
    with open("advent8_input.txt", "r") as f:
        array2D = []
        for line in f.readlines():
            array2D.append(list(line)[:-1])
    return array2D

def see_edge(left, right, top, bot, tree):
    return not(max(left) < tree or max(right) < tree or max(top) < tree or max(bot) < tree)


def get_scenic_score(left, right, top, bot, tree):
    product = 1
    for arr in [left, right, top, bot]:
        for idx, tr in enumerate(arr):
            if (tr) >= tree:
                break
        product *= idx + 1
    return product

def scan_trees(array2D, part):
    mask = np.ones(array2D.shape)
    rows = array2D.shape[0]
    cols = array2D.shape[1]
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            tree = array2D[i,j]
            left = array2D[i,:j]
            right = array2D[i,j+1:]
            top = array2D[:i,j]
            bot = array2D[i+1:,j]
            if part == 1:
                mask[i,j] = 0 if see_edge(left, right, top, bot, tree) else 1
            else:
                mask[i,j] = get_scenic_score(np.flip(left), right, np.flip(top), bot, tree)
    if part == 1:
        print(sum(sum(mask)))
    else: 
        print(np.amax(mask))

def part1():
    array2D = np.array(init()) 
    print("Part 1")
    scan_trees(array2D, 1)

def part2():
    array2D = np.array(init()) 
    print("Part 2")
    scan_trees(array2D, 2)


def main():
    part1()
    part2()
    return 0


if __name__ == "__main__":
    main()