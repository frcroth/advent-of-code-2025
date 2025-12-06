from functools import reduce

def split_line(line:str):
    line = line.replace("  ", " ")
    line = line.replace("  ", " ")
    line = line.replace("  ", " ")
    return line.strip().split(" ")

def parse(path, numberlines=3):
    with open(path) as f:
        lines = f.readlines()
    numbers = lines[:numberlines]
    operations = lines[numberlines]
    numbers = list(zip(*[[int(a) for a in split_line(line)] for line in numbers]))
    operations = split_line(operations)
    return numbers, operations

def part_1(input):
    numbers = input[0]
    operations = input[1]
    
    total = 0
    for i, op in enumerate(operations):
        if op == "+":
            total += sum(numbers[i])
        if op == "*":
            total += reduce(lambda x,y : x * y,numbers[i], 1)
    return total

def parse_cephalod_numbers(path, numberlines = 3):
    
    with open(path) as f:
        lines = f.readlines()
        
    operations_line = lines[numberlines]
    problems = []
    nums = []
    
    for k in range(len(operations_line)):
        i = len(operations_line) - 1 - k
        digits = ""
        for j in range(numberlines):
            digits += lines[j][i]
        if digits == " " * numberlines:
            continue
        nums.append(int(digits))
        if operations_line[i] != " ":
            problems.append((nums, operations_line[i]))
            nums = []
    return problems
    
def part_2(problems):
    total = 0
    for problem in problems:
        op = problem[1]
        numbers = problem[0]
        if op == "+":
            total += sum(numbers)
        if op == "*":
            total += reduce(lambda x,y : x * y,numbers, 1)
    return total

if __name__ == "__main__":
    example = parse("example.txt")
    assert 4277556 == part_1(example)
    
    input = parse("input.txt", 4)
    print(part_1(input))
    
    ceph_example = parse_cephalod_numbers("example.txt")
    assert 3263827 == part_2(ceph_example)
    
    ceph_input= parse_cephalod_numbers("input.txt", 4)
    print(part_2(ceph_input))