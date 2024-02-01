
def init_crates(crates):
    indexes = list(crates[-1])
    test =  [num for num in list(crates[-1]) if num != ' ']
    piles = []
    for elem in test:
        current_pile = []
        crate_nb = indexes.index(elem)
        for l in range(len(crates)-2, -1, -1):
            if(list(crates[l])[crate_nb] != ' '):
                current_pile.append(list(crates[l])[crate_nb])
        piles.append(current_pile)
    return piles

def move_crates (piles, moves):
    for move in moves:
        _, amount, _, move_from, _, move_to = move.split()
        for a in range(int(amount)):
            crate = piles[int(move_from) -1][-1]
            piles[int(move_from) -1].pop()
            piles[int(move_to) -1].append(crate)
    return piles

def move_crates_keeping_order(piles, moves):
    for move in moves:
        _, amount, _, move_from, _, move_to = move.split()
        crates = piles[int(move_from)-1][len(piles[int(move_from)-1])-int(amount):]
        for a in range(int(amount)):
            piles[int(move_from)-1].pop()
        for crate in crates:
            piles[int(move_to) -1].append(crate)
    return piles

def get_last_crate(piles):
    top = ''
    for pile in piles:
        top += pile[-1]
    print(top)

def part1(piles, moves):
        piles = move_crates(piles, moves[1:])
        get_last_crate(piles)

def part2(piles, moves):
    piles = move_crates_keeping_order(piles, moves[1:])
    get_last_crate(piles)

def init():
    with open("advent5_input.txt", "r") as f: #advent5_input
        crates = []
        moves = []
        crates_idx = -1
        for i, line in enumerate(f.read().splitlines()):
            if not line.startswith('move') and not line == '':
                crates.append(line)
            else:
                moves.append(line)
        piles = init_crates(crates)
    return piles, moves

def main():
    piles, moves = init()
    print("Part 1")
    part1(piles, moves)
    piles, moves = init()
    print("Part 2")
    part2(piles, moves)
    return 0




if __name__ == "__main__":
    main()