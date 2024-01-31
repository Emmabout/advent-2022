
value_me = {"X": 1, "Y": 2, "Z":3}
value_them = {"A": 1, "B": 2, "C":3}
beats = {1:3, 2:1, 3:2}
loses = {1:2, 2:3, 3:1}

def game_result(them, me):
    if(value_them[them] == value_me[me]):
        #Draw
        return 3
    if(beats[value_them[them]] == value_me[me]):
        #Lost
        return 0
    #Won
    return 6

def part1():
    with open("advent2_input.txt", "r") as f: #advent2_input
        score = 0
        for line in f.read().splitlines():
            them, me = line.split(' ')
            result = game_result(them, me)
            score += result + value_me[me]
        print(score)

def choose_shape(them, outcome):
    if outcome == 'X':
        return beats[value_them[them]] + 0
    if outcome == 'Y':
        return value_them[them] + 3
    if outcome == 'Z':
        return loses[value_them[them]] + 6



def part2():
    with open("advent2_input.txt", "r") as f: #advent2_input
        score = 0
        for line in f.read().splitlines():
            them, outcome = line.split(' ')
            round = choose_shape(them, outcome)
            score += round
        print(score)

def main():
    print("Part 1")
    part1()
    print("Part 2")
    part2()
    return 0




if __name__ == "__main__":
    main()