import itertools

a = [i for i in range(0,100)]
b = [i for i in range(0,100)]
# result contains all possible combinations.
combinations = list(itertools.product(a,b))

OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_HALT = 99

def search_pair(positions, target):
    combo = 0
    while combo < len(combinations):
        cur = 0
        # reset program memory
        cur_positions = positions.copy()
        noun, verb = combinations[combo]
        if intcode(cur_positions, noun, verb) == target: break
        combo += 1
    return combinations[combo]

def intcode(positions, noun, verb):
    cur = 0
    positions[1], positions[2] = noun, verb
    while cur < len(positions):
        opcode = positions[cur]
        if opcode == OPCODE_HALT:
            break
        # print(cur, len(positions))
        if opcode == OPCODE_ADD:
            # print(positions[cur+3])
            positions[positions[cur+3]] = positions[positions[cur+1]] + positions[positions[cur+2]]
        elif opcode == OPCODE_MULTIPLY:
            positions[positions[cur+3]] = positions[positions[cur+1]] * positions[positions[cur+2]]
        cur += 4
    return positions[0]

with open('input.txt','r') as f:
    cur = 0
    positions = f.read().split(',')
    positions = list(map(int, positions))
    # part 1
    print('position at 0', intcode(positions.copy(), 12, 2))
    # part 2
    v1, v2 = search_pair(positions.copy(), 19690720)
    print(v1, v2, intcode(positions.copy(), v1, v2))

