# /// script
# dependencies = [
#   "z3-solver"
# ]
# ///


from z3 import *

def parse_machine(line):
    lights = line.split(" ")[0]
    lights = lights[1:-1]
    
    buttons = line.split(" ")[1:-1]
    buttons = [[int(a) for a in b[1:-1].split(",")] for b in buttons]
    
    joltage = [int(j) for j in line.strip().split(" ")[-1][1:-1].split(",")]
    
    return lights, buttons, joltage

def parse_input(path):
    with open(path) as f:
        lines = f.readlines()
        return [parse_machine(l) for l in lines]
    
def flip(lights, button):
    new_lights = list(lights)
    for flip in button:
        if new_lights[flip] == ".":
            new_lights[flip] = "#"
        else:
            new_lights[flip] = "."
    return "".join(new_lights)

def states_iteration(states_dict: dict, buttons: list):
    new_dict = states_dict.copy()
    for state, buttons_thus_far in states_dict.items():
            for button_idx, button in enumerate(buttons):
                next_state = flip(state, button)
                if next_state in states_dict:
                    pass
                    # We should be able to ignore it, since we brute force all button, the existing way to get to that state has <= number of buttons
                else:
                    new_dict[next_state] = [*buttons_thus_far, button_idx]
                    return new_dict
    print("NO CHANGES")
    return new_dict
    
def solve_machine_lights(machine):
    
    final_lights = machine[0]
    buttons = machine[1]
    
    initial_state = "." * len(final_lights)
    
    state_directory = {initial_state : []}
    
    while True:
        state_directory = states_iteration(state_directory, buttons)
        if final_lights in state_directory:
            break
        
    return len(state_directory[final_lights])

def part_1(machines):
    return sum([solve_machine_lights(m) for m in machines])

def solve_machine_joltages(machine):
    buttons = machine[1]
    joltages = machine[2]
    
    n = len(joltages)
    
    vectors = []
    for b in buttons:
        base = [0] * n
        for k in b:
            base[k] = 1
        vectors.append(base)
    
    m = len(vectors)

    # Each coefficient (x_n) is how often we press a button
    xs = [Int(f"x_{i}") for i in range(m)]
    opt = Optimize()
    
    for x in xs:
        opt.add(x >= 0) # We cant press buttons a negative amount of times

    for j in range(n):
        constraint = Sum([ (vectors[i][j] * xs[i]) for i in range(m) ])
        opt.add(constraint == joltages[j])

    opt.minimize(sum(xs))

    if opt.check() == sat:
        model = opt.model()
        coeffs = [ model[x].as_long() for x in xs]
        return sum(coeffs)
    else:
        print("UNSOLVABLE")

    
def part_2(machines):
   return sum([solve_machine_joltages(m) for m in machines])
    
if __name__ == "__main__":
    example_machines = parse_input("example.txt")
    
    assert 7 == part_1(example_machines)
    
    input_machines = parse_input("input.txt")
    
    print(part_1(input_machines))
    
    assert 33 == part_2(example_machines)
    
    print(part_2(input_machines))
    
    