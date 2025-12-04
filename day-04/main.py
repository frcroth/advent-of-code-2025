
def get_example():
    with open("example.txt") as f:
        example = f.readlines()
        example = [list(a.strip()) for a in example]
    return example

def get_input():
    with open("input.txt") as f:
        i = f.readlines()
        i = [list(a.strip()) for a in i]
    return i

def safe_lookup(x, y, matrix):
    if y < 0 or x < 0 or y >= len(matrix) or x >= len(matrix[0]):
        return "."
    return matrix[y][x]


def get_adjacents(x, y, matrix):
    return [
        safe_lookup(x - 1, y, matrix),
        safe_lookup(x - 1, y + 1, matrix),
        safe_lookup(x - 1, y - 1, matrix),
        safe_lookup(x, y + 1, matrix),
        safe_lookup(x, y - 1, matrix),
        safe_lookup(x + 1, y - 1, matrix),
        safe_lookup(x + 1, y, matrix),
        safe_lookup(x + 1, y + 1, matrix),
    ]

def part_1(input):
    accessible = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != "@":
                continue
            adjacents = get_adjacents(x, y, input)
            rolls = [a for a in adjacents if a == "@"]
            if len(rolls) < 4:
                accessible += 1

    return accessible

def get_all_accessible(matrix):
    accessibles = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] != "@":
                continue
            adjacents = get_adjacents(x, y, matrix)
            rolls = [a for a in adjacents if a == "@"]
            if len(rolls) < 4:
                accessibles.append([x, y])

    return accessibles

def part_2(input):
    total_taken = 0
    while True:
        accessibles = get_all_accessible(input)
        if len(accessibles) == 0:
            break
        total_taken += len(accessibles)
        for a in accessibles:
            input[a[1]][a[0]] = "."
    return total_taken

if __name__ == "__main__":
    assert 13 == part_1(get_example())
    assert 43 == part_2(get_example())
    
    print(part_1(get_input()))
    print(part_2(get_input()))
