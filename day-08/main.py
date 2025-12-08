from collections import Counter

def parse(path):
    with open(path) as f:
        lines = f.readlines()
        return [[float(a) for a in l.split(",")] for l in lines]

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** (1/2)

def part_1(coords, connections = 10):
    # Brute force
    
    distances = dict()
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            d = dist(coords[i], coords[j])
            distances[(i,j)] = d
            #distances [(j,i)] = d
            
    circuits = dict()
    
    entries = list(distances.items())
    entries.sort(key=lambda p: p[1])
    circuit_id = 1
    steps = 0
    for e in entries:
        if len(circuits) == len(coords):
            break
        boxes = e[0]
        a = boxes[0]
        b = boxes[1]
        current_circuit_a = circuits.get(a)
        current_circuit_b = circuits.get(b)
        if not current_circuit_a and not current_circuit_b:
            # New circuit
            circuits[a] = circuit_id
            circuits[b] = circuit_id
            circuit_id += 1
        # Adding to existing circuit
        elif current_circuit_a and not current_circuit_b:
            circuits[b] = circuits[a]
        elif not current_circuit_a and current_circuit_b:
            circuits[a] = circuits[b]
        # Combining two circuits
        elif current_circuit_a and current_circuit_b and current_circuit_b != current_circuit_a:
            for key in circuits:
                if circuits[key] == current_circuit_a or circuits[key] == current_circuit_b:
                    circuits[key] = circuit_id
            circuit_id += 1
        steps += 1
        if steps >= connections:
            break
        
    circuit_sizes = list(Counter(circuits.values()).values())
    circuit_sizes.sort(reverse=True) # Sanity Check
    top_three = circuit_sizes[0:3]
    return top_three[0] * top_three[1] * top_three[2]

def part_2(coords):
    # Copied from part 1 with only slight adjustments
    
    distances = dict()
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            d = dist(coords[i], coords[j])
            distances[(i,j)] = d
            
    circuits = dict()
    
    entries = list(distances.items())
    entries.sort(key=lambda p: p[1])
    circuit_id = 1
    for e in entries:
        boxes = e[0]
        a = boxes[0]
        b = boxes[1]
        current_circuit_a = circuits.get(a)
        current_circuit_b = circuits.get(b)
        if not current_circuit_a and not current_circuit_b:
            circuits[a] = circuit_id
            circuits[b] = circuit_id
            circuit_id += 1
        elif current_circuit_a and not current_circuit_b:
            circuits[b] = circuits[a]
        elif not current_circuit_a and current_circuit_b:
            circuits[a] = circuits[b]
        elif current_circuit_a and current_circuit_b and current_circuit_b != current_circuit_a:
            for key in circuits:
                if circuits[key] == current_circuit_a or circuits[key] == current_circuit_b:
                    circuits[key] = circuit_id
            circuit_id += 1
        i += 1
        if len(circuits) == len(coords) and len(set(circuits.values())) == 1:
            return int(coords[a][0] * coords[b][0])

if __name__ == "__main__":
    example = parse("example.txt")
    assert 40 == part_1(example)
    
    input = parse("input.txt")
    print(part_1(input, 1000))
    
    assert 25272 == part_2(example)
    print(part_2(input))
    
    
    
    
    
