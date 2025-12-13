def parse(file):
    
    with open(file) as f:
        input = f.read()
    
    parts = input.split("\n\n")
    regions = parts[-1].split("\n")
    shapes = parts[:-1]
    
    parsed_shapes = []
    
    for shape in shapes:
        shape = shape.split("\n")
        shape_lines = shape[1:]
        width = len(shape_lines[0])
        height = len(shape_lines)
        parsed_shapes.append((shape_lines, width, height))
    
    parsed_regions = []
    
    for region in regions:
        size = region.split(": ")[0]
        width = int(size.split("x")[0])
        height = int(size.split("x")[1])
        indices = [int(a) for a in region.split(": ")[1].split(" ")]
        parsed_regions.append((width, height, indices))
        
        
    return parsed_shapes, parsed_regions


def part_1(parsed_input):
    parsed_shapes, parsed_regions = parsed_input
    for shape in parsed_shapes:
        assert shape[1] == 3
        assert shape[2] == 3
    possible_regions = 0
    
    for r in parsed_regions:
        presents = sum(r[2])
        if (r[0] // 3) * (r[1] // 3) >= presents:
            possible_regions += 1
    return possible_regions
        
if __name__ == "__main__":
    example_parsed = parse("example.txt")
    # Example does not work for the shortcut
    example = 2
    assert 2 == example
    
    input_parsed = parse("input.txt")
    print(part_1(input_parsed))
    