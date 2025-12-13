import os


def read_input(path):
    with open(path) as f:
        return f.readlines()
    
def part_1(input: list[str]):
    # First line is start
    start_index = input[0].index("S")
    streams = [start_index]
    next_streams = []
    splits = 0
    for i, l in enumerate(input[1:]):
        next_streams = []
        for stream in streams:
            if l[stream] == ".":
                # Continue moving down
                next_streams.append(stream)
            elif l[stream] == "^":
                # Split
                splits += 1
                next_streams.append(stream-1)
                next_streams.append(stream+1)
        streams = list(set(next_streams))
    return splits

def part_2(input: list[str]):
    # First line is start
    start_index = input[0].index("S")
    streams = [start_index]
    next_streams = []
    splits = 0
    particles = [[0] * len(input[0]) for _ in range(len(input))]
    particles[0][start_index] = 1
    for i, l in enumerate(input[1:]):
        next_streams = []
        step = i + 1
        for stream in streams:
            if l[stream] == ".":
                # Continue moving down
                next_streams.append(stream)
                particles[step][stream] += particles[step-1][stream]
            elif l[stream] == "^":
                # Split
                splits += 1
                next_streams.append(stream-1)
                next_streams.append(stream+1)
                
                
                particles[step][stream-1] += particles[step-1][stream]
                particles[step][stream+1] += particles[step-1][stream]
        streams = list(set(next_streams))
    return sum(particles[-1])
    
if __name__ == "__main__":
    example = read_input("example.txt")
    assert 21 == part_1(example)
    assert 40 == part_2(example)
    
    if not os.getenv("SKIP_INPUT"):
        input = read_input("input.txt")
        print(part_1(input))
        print(part_2(input))