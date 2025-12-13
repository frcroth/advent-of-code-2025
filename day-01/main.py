import re
import os

regex = r"([LR])(\d+)"


def read_example():
    with open("example.txt") as f:
        return f.readlines()


def read_input():
    with open("input.txt") as f:
        return f.readlines()


def ceil(x):
    if int(x) != x:
        return int(x) + 1
    return x


def solve(input):
    # Parse
    data = []
    for l in input:
        matches = re.findall(regex, l, re.MULTILINE)
        data.append(matches[0])

    # Part 1
    dial = 50
    zero_times = 0
    for d in data:
        if d[0] == "L":
            dial = (dial - int(d[1])) % 100
        else:
            dial = (dial + int(d[1])) % 100
        if dial == 0:
            zero_times += 1

    part_2 = 0
    dial = 50

    i = 0
    for d in data:
        turn_val = int(d[1])
        if d[0] == "L":
            while turn_val > 100:
                part_2 += 1
                turn_val -= 100
            if dial - turn_val <= 0 and dial != 0:
                part_2 += 1
            dial = (dial - turn_val) % 100
        else:
            while turn_val > 100:
                part_2 += 1
                turn_val -= 100
            if dial + turn_val >= 100 and dial != 0:
                part_2 += 1
            dial = (dial + turn_val) % 100
        i += 1

    return zero_times, part_2


if __name__ == "__main__":
    example = read_example()
    assert solve(example) == (3, 6)

    if not os.getenv("SKIP_INPUT"):
        input = read_input()
        print(solve(input))
