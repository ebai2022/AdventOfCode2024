from collections import defaultdict
import copy

# states: upwards (-1, 0), right (0, 1), down (-1, 0), left (0, -1)
states = [(-1, 0), (0, 1), (1, 0), (0, -1)]
test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

def find_distinct_positions(matrix, start):
    state = 0
    seen = set()
    while True:
        i, j = start
        seen.add(start)
        next_start = (i + states[state][0], j + states[state][1])
        if is_valid(matrix, next_start):
            if matrix[next_start[0]][next_start[1]] == "#":
                state = (state + 1) % 4
                next_start = (i + states[state][0], j + states[state][1])
            start = next_start
        else:
            break
    return len(seen)


def find_possible_loops(matrix, start):
    n, m = len(matrix), len(matrix[0])
    total = 0
    for i in range(n):
        for j in range(m):
            print(f"processing {i, j}")
            if matrix[i][j] == "#" or matrix[i][j] == "^":
                continue
            # empty square, put an obstacle and traverse
            deepcopy = copy.deepcopy(matrix)
            assert deepcopy == matrix
            deepcopy[i][j] = "#"
            if find_loop(deepcopy, start[0], start[1]):
                total += 1
    return total


def find_loop(deepcopy, x, y):
    n, m = len(deepcopy), len(deepcopy[0])
    direction = 0
    visited = set()
    while x >= 0 and x < n and y >= 0 and y < m:
        # check if we have already visited the place in the same orientation (loop found)
        if (x, y, direction) in visited:
            # print(f"visited {x, y, direction} before")
            return True
        visited.add((x, y, direction))
        # continue traversing
        adjacent_walls = 0
        current_direction = states[direction]
        for i in range(4):
            # print(f"current direction: {current_direction}")
            # if the next step is out of bounds, this is not a loop since we have exited the maze
            nx, ny = x + current_direction[0], y + current_direction[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return False
            # print(f"trying next square: {nx, ny}")
            # find the first non wall
            if deepcopy[nx][ny] != "#":
                break
            direction = (direction + 1) % 4
            adjacent_walls += 1
            # change the direction
            current_direction = states[direction]
        # if we are surrounded by walls, return True (SHOULD NEVER BE TRUE)
        assert adjacent_walls < 4
        # otherwise, continue traversing
        x = x + current_direction[0]
        y = y + current_direction[1]
    # no loop found
    return False

def is_valid(matrix, start):
    n, m = len(matrix), len(matrix[0])
    i, j = start
    if i >= 0 and i < n and j >= 0 and j < m:
        return True


if __name__ == "__main__":
    with open("Day 6/input.txt", "r") as file:
        data = file.read().splitlines()
    # data = test_input.splitlines()
    n, m = len(data), len(data[0])
    matrix = [["."] * m for _ in range(n)]
    row = 0
    for line in data:
        for i in range(m):
            matrix[row][i] = line[i]
            if line[i] == "^":
                start = (row, i)
        row += 1
    print(find_distinct_positions(matrix, start))
    print(find_possible_loops(matrix, start))