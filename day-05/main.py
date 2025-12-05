def parse_input(path):
    with open(path) as f:
        all = f.read()
    parts = all.split("\n\n")
    ranges_raw = parts[0]
    ranges = []
    for r in ranges_raw.split("\n"):
        start = int(r.split("-")[0])
        end = int(r.split("-")[1])
        ranges.append((start, end))
    
    available = [int(a) for a in parts[1].split("\n")]
    return ranges, available

def part_1(input):
    ranges: list = input[0]
    available = input[1]
    
    ranges.sort(key=lambda x: x[0])
    
    fresh = 0
    # Brute force
    
    def is_fresh(ingredient):
        for r in ranges:
            if ingredient >= r[0] and ingredient <= r[1]:
                return True
        return False
    
    for ingredient in available:
        if is_fresh(ingredient):
            fresh += 1
                
    return fresh

def fix_overlapping_ranges(ranges: list):
    ranges.sort(key=lambda x: x[0])
    for (i,r) in enumerate(ranges):
        for j, r2 in enumerate(ranges[i+1:]):
            second_index = j + i + 1
            # start of r2 is guaranteed bigger than start of r now because we sorted before
            assert r2[0] >= r[0]
            if r2[0] <= r[1]:
                # Overlap!
                # r  ----------------
                # r2      ------
                
                # We can thus count only r!
                if r2[1] <= r[1]:
                    del ranges[second_index]
                    return fix_overlapping_ranges(ranges)
                    
                
                # or
                # r  ----------------
                # r2        -------------
                
                # We can then ignore the overlapping part for further calculations!
                else:
                    ranges[second_index] = (r[1]+1, r2[1])
                    return fix_overlapping_ranges(ranges)
                
    return ranges

    
def part_2(input):
    
    ranges: list = input[0]
    ranges.sort()
    # Find overlapping ranges
    ranges = fix_overlapping_ranges(ranges)
    
    # Now overlappings anymore :fingers_crossed:
    
    return sum([r[1]-r[0]+1 for r in ranges])
    

if __name__ == "__main__":
    example = parse_input("example.txt")
    assert 3 == part_1(example)
    
    input = parse_input("input.txt")
    print(part_1(input))
    
    assert 14 == part_2(example)
    
    print(part_2(input))