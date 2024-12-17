from collections import deque
import heapq

test_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


# directions: 0 east, 1 south, 2 west, 3 north
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijkstra(matrix, start):
    q = [(0, 0, start[0], start[1])]
    seen = set()
    while q:
        weight, direction, x, y = heapq.heappop(q)
        if matrix[x][y] == "E":
            return weight
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i, coords in enumerate(directions):
            dx, dy = coords
            if x + dx >= 0 and x + dx < len(matrix) and y + dy >= 0 and y + dy < len(matrix[0]) and matrix[x + dx][y + dy] != "#":
                if i == direction:
                    heapq.heappush(q, (weight + 1, i, x + dx, y + dy))
                elif abs(i - direction) == 2:
                    continue
                else:
                    heapq.heappush(q, (weight + 1001, i, x + dx, y + dy))
    return 0


if __name__ == "__main__":
    with open("Day 16/input.txt") as file:
        data = file.read().splitlines()
    data = test_input.splitlines()
    matrix = []
    start = (0, 0)
    for i, line in enumerate(data):
        matrix.append([])
        for j in range(len(line)):
            matrix[i].append(line[j])
            if line[j] == "S":
                start = (i, j)
    print(dijkstra(matrix, start))
    # for line in matrix:
    #     print(line)