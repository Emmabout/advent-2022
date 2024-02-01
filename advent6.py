import numpy as np


def init():
    with open("advent6_input.txt", "r") as f: #advent6_input
        stream = f.read()
    return stream

def delete_pos_from_mask(mask, pos1, pos2, message_length):
    diff = pos2-pos1
    low_idx = message_length-diff
    mask[max(0,pos1-low_idx+1):min(len(mask), pos1+1)] = 0
    return mask

def get_marker(mask, message_length):
    marker =next((index for index,value in enumerate(mask) if value != 0), None) + message_length
    print(marker)
    return marker

def decode(stream, message_length):
    stream_list = list(stream)
    unique = np.unique(stream_list)
    mask = np.ones(len(stream_list))
    for letter in unique:
        occurences = [i for i, x in enumerate(stream_list) if x == letter]
        for i, oc in enumerate(occurences[:-1]):
            if occurences[i+1] - oc <= message_length-1:
                mask = delete_pos_from_mask(mask, oc, occurences[i+1], message_length)
    get_marker(mask, message_length)

def part1():
    stream = init()
    decode(stream, 4)

def part2():
    stream = init()
    decode(stream, 14)

def main():
    print("Part 1")
    part1()
    print("Part 2")
    part2()
    return 0


if __name__ == "__main__":
    main()