from collections import deque

test_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start, seen):
    q = deque([start])
    plant = matrix[start[0]][start[1]]
    perimeter, area, sides = 0, 0, 0
    curr_seen = set()
    perimeter_coords = set()
    while q:
        i, j = q.popleft()
        if (i, j) in curr_seen:
            continue
        if matrix[i][j] == plant:
            area += 1
        else:
            if (
                (i - 1, j) not in perimeter_coords
                and (i + 1, j) not in perimeter_coords
                and (i, j - 1) not in perimeter_coords
                and (i, j + 1) not in perimeter_coords
            ):
                print(f"new side starting at {i, j}")
                sides += 1
            perimeter_coords.add((i, j))
            perimeter += 1
            continue
        seen.add((i, j))
        curr_seen.add((i, j))
        for x, y in directions:
            ni, nj = i + x, j + y
            walli, wallj = i + (0.6 * x), j + (0.6 * y)
            if (
                ni >= 0
                and ni < len(matrix)
                and nj >= 0
                and nj < len(matrix[0])
                and matrix[ni][nj] == plant
            ):
                q.append((ni, nj))
            else:
                if (
                    (walli - 1, wallj) not in perimeter_coords
                    and (walli + 1, wallj) not in perimeter_coords
                    and (walli, wallj - 1) not in perimeter_coords
                    and (walli, wallj + 1) not in perimeter_coords
                ):
                    sides += 1
                    print(f"new side starting at {walli, wallj}")
                else:
                    print(f"continuing wall at {walli, wallj}")
                perimeter_coords.add((walli, wallj))
                perimeter += 1
    if sides % 2 != 0:
        sides = sides - 1
    return perimeter, area, sides


if __name__ == "__main__":
    with open("Day 12/input.txt") as file:
        data = file.read().splitlines()
    # data = test_input.splitlines()
    n, m = len(data), len(data[0])
    matrix = [["."] * m for _ in range(n)]
    for i, line in enumerate(data):
        for j in range(len(line)):
            matrix[i][j] = line[j]
    # print(matrix)
    seen = set()
    price_full = 0
    price_discount = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in seen:
                curr_perm, curr_area, sides = bfs((i, j), seen)
                print(
                    f"perimeter {curr_perm} and area {curr_area} and sides {sides} for {matrix[i][j]}"
                )
                price_full += curr_area * curr_perm
                price_discount += curr_area * sides
    print(price_full)
    print(price_discount)
