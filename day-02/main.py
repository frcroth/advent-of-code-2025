import os

def read_example():
    with open("example.txt") as f:
        return f.readlines()[0].split(",")
    
def read_input():
    with open("input.txt") as f:
        return f.readlines()[0].split(",")
    
def is_valid_id(id: str):
    has_leading_zeros = id.startswith("0")
    if has_leading_zeros:
        return False
    if len(id) % 2 != 0:
        return False
    middle = int(len(id)/2)
    return id[0:middle] == id[middle:]

def is_repeated_id(id: str):
    for pattern_len in range(1, int(len(id)/2)+1):
        if id == id[0:pattern_len] * int(len(id)/pattern_len):
            return True
    return False


def part_1(input):
    id_sum = 0
    for line in input:
        rang = line.split("-")
        a = int(rang[0])
        b = int(rang[1])
        for i in range(a,b):
            id = str(i)
            if is_valid_id(id):
                id_sum += i
    return id_sum

def part_2(input):
    id_sum = 0
    for line in input:
        rang = line.split("-")
        a = int(rang[0])
        b = int(rang[1])
        for i in range(a,b+1):
            id = str(i)
            if is_repeated_id(id):
                id_sum += i
    return id_sum


if __name__ == "__main__":
    example = read_example()
    assert 1227775532 == part_1(example)
    assert 4174379265 == part_2(example)
    
    if not os.getenv("SKIP_INPUT"):
        print(part_1(read_input()))
        print(part_2(read_input()))
