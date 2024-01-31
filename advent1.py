
def advent():
    with open("advent1_input.txt", "r") as f: #advent1_input
        top_elves = []
        somme = 0
        biggest = 0
        for line in f.read().splitlines():
            if line == "":
                if(somme > biggest):
                    biggest = somme
                top_elves.append(somme)
                somme = 0
            else:
                somme += int(line)
        top_elves.append(somme)
    print(biggest)
    top_elves.sort(reverse=True)
    print(top_elves)
    total = sum(top_elves[:3])
    print(total)
    return top_elves

def main():
    advent()
    return 0




if __name__ == "__main__":
    main()