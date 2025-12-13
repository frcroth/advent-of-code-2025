import os


def read_example():
    with open("example.txt") as f:
        return [s.strip() for s in f.readlines()]
    
def read_input():
    with open("input.txt") as f:
        return [s.strip() for s in f.readlines()]


def get_bank_val(bank):
    nums = [int(a) for a in bank]
    relevant_nums = nums[:-1]
    m = max(relevant_nums)
    first_occurrence = nums.index(m)
    next_highest = max(nums[first_occurrence+1:])
    full = int(str(m) + str(next_highest))
    return full


def part_1(input):
    return sum([get_bank_val(bank) for bank in input])


def get_bank_val_part_2(bank):
    nums = [int(a) for a in bank]
    full_num = []
    search_start_index = 0
    for k in range(12,0,-1):
        if k == 1:
            remaining = nums[search_start_index:]
            full_num.append(max(remaining))
            break
        relevant_nums = nums[search_start_index:-(k-1)]
        m = max(relevant_nums)
        full_num.append(m)
        # Now search only after m
        search_start_index = relevant_nums.index(m) + search_start_index + 1
    full = int("".join([str(a) for a in full_num]))
    return full

def part_2(input):
    return sum([get_bank_val_part_2(bank) for bank in input])

if __name__ == "__main__":
    example = read_example()
    assert 357 == part_1(example)
    assert 3121910778619 == part_2(example)

    if not os.getenv("SKIP_INPUT"):
        input = read_input()
        print(part_1(input))
        print(part_2(input))
