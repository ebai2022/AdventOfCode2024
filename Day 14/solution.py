import re
from collections import defaultdict

verify_matrix = """1.12.......
...........
...........
......11.11
1.1........
.........1.
.......1..."""

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
WIDTH = 101
HEIGHT = 103

def simulate(positions, velocity, iterations):
    min_safety_factor = float('inf')
    min_index = -1
    for i in range(iterations):
        for robot in positions:
            vx, vy = velocity[robot]
            x, y = positions[robot]
            positions[robot] = ((x + vx) % WIDTH, (y + vy) % HEIGHT)
        factor = safety_factor(positions)
        if factor < min_safety_factor:
            min_safety_factor = factor
            min_index = i
    return min_index + 1

def safety_factor(positions):
    tl, tr, bl, br = 0, 0, 0, 0
    half_row, half_col = WIDTH // 2, HEIGHT // 2
    for robot in positions:
        x, y = positions[robot]
        if x < half_row and y < half_col:
            tl += 1
        elif x < half_row and y > half_col:
            tr += 1
        elif x > half_row and y < half_col:
            bl += 1
        elif x > half_row and y > half_col:
            br += 1
    return tl * tr * bl * br


if __name__ == "__main__":
    with open("Day 14/input.txt") as file:
        data = file.read().splitlines()
    velocity = defaultdict(tuple)
    positions = defaultdict(tuple)
    for i, line in enumerate(data):
        x, y, vx, vy = re.findall(r"(-?\d+)", line)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        velocity[i] = (vx, vy)
        positions[i] = (x, y)
    print(simulate(positions, velocity, 10000))
    # print(safety_factor(positions))