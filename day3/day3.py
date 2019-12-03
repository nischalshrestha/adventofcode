import itertools

def find_pts(directions):
    # Keep track of current x and y for wire
    x = 0
    y = 0
    pts = []
    for d in directions:
        if d[0] == 'L':
            pts.extend([(x - pt, y) for pt in range(1, d[1]+1)])
        elif d[0] == 'R':
            pts.extend([(x + pt, y) for pt in range(1, d[1]+1)])
        elif d[0] == 'D':
            pts.extend([(x, y - pt) for pt in range(1, d[1]+1)])
        elif d[0] == 'U':
            pts.extend([(x, y + pt) for pt in range(1, d[1]+1)])
        x, y = pts[-1]
    return pts

def manhattan_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def steps(pts, intersection):
    i = 0
    pt = pts[i]
    while i < len(pts) and pt != intersection:
        pt = pts[i]
        i += 1
    return i

with open('input.txt','r') as f:
    # Part 1
    # For each line (wire) need to figure out its path points
    origin = (0, 0)
    # Split each line to look at each direction
    wires = f.readlines()
    wire1 = wires[0].rstrip().split(',')
    wire2 = wires[1].rstrip().split(',')
    # Unwrangle direction by a tuple
    wire1_directions = [(d[0], int(d[1:])) for d in wire1]
    wire2_directions = [(d[0], int(d[1:])) for d in wire2]
    # Find pts for each wire
    wire1_pts = find_pts(wire1_directions)
    wire2_pts = find_pts(wire2_directions)
    # Find intersections
    intersections = list(set(wire1_pts).intersection(set(wire2_pts)))
    dists = []
    # Find closest manhattan dist btw points
    for i in intersections:
        dists.append(manhattan_dist(origin, i))
    print(f'min dist: {min(dists)}')
    # Part 2
    wire_steps_to_intersection = lambda x, y: [steps(x, i) for i in y]
    # Find number of steps for each wire to reach intersections
    wire1_steps =  wire_steps_to_intersection(wire1_pts, intersections)
    wire2_steps =  wire_steps_to_intersection(wire2_pts, intersections)
    print(f'min combo: {min([sum((w1, w2)) for w1, w2 in zip(wire1_steps, wire2_steps)])}')

