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
    # for _ in range(iterations):
    #     for robot in positions:
    #         vx, vy = velocity[robot]
    #         x, y = positions[robot]
    #         # print(((x + vx) % NUM_ROWS, (y + vy) % NUM_COLS))
    #         positions[robot] = ((x + vx) % NUM_ROWS, (y + vy) % NUM_COLS)
    for robot in positions:
        vx, vy = velocity[robot]
        x, y = positions[robot]
        # positions[robot] = ((x + vx * 100) % NUM_ROWS, (y + vy * 100) % NUM_COLS)

def safety_factor(positions):
    tl, tr, bl, br = 0, 0, 0, 0
    half_row, half_col = WIDTH // 2, HEIGHT // 2
    for robot in positions:
        x, y = positions[robot]
        if x < half_row and y < half_col:
            # print(f"robot {robot} in top left at {x, y}")
            tl += 1
        elif x < half_row and y > half_col:
            # print(f"robot {robot} in top right at {x, y}")
            tr += 1
        elif x > half_row and y < half_col:
            # print(f"robot {robot} in bottom left at {x, y}")
            bl += 1
        elif x > half_row and y > half_col:
            # print(f"robot {robot} in bottom right at {x, y}")
            br += 1
        else:
            print(f"robot {robot} not in a quadrant at {x, y}")
    print(tl, tr, bl, br)
    return tl * tr * bl * br


if __name__ == "__main__":
    with open("Day 14/input.txt") as file:
        data = file.read().splitlines()
    # data = test_data.splitlines()
    # matrix = [[-1] * NUM_COLS for _ in range(NUM_ROWS)]  # -1 means empty
    velocity = defaultdict(tuple)
    positions = defaultdict(tuple)
    for i, line in enumerate(data):
        x, y, vx, vy = re.findall(r"(-?\d+)", line)
        # match = re.search(r"p=(-?\d+),(-?\d+)", line)
        # x, y = int(match.group(1)), int(match.group(2))
        # positions[i] = (x, y)
        # match = re.search(r"v=(-?\d+),(-?\d+)", line)
        # vx, vy = int(match.group(1)), int(match.group(2))
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        velocity[i] = (vx, vy)
        nx, ny = x + vx * 100, y + vy * 100
        nx = nx % WIDTH
        ny = ny % HEIGHT
        if nx < 0 or ny < 0:
            print("BROKE")
        positions[i] = (nx, ny)
    # print(positions)
    # print(velocity)
    # simulate(positions, velocity, 100)
    print(safety_factor(positions))