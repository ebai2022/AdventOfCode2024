from collections import deque

test_data = """012345
123456
234567
345678
4.6789
56789."""

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def process_trails(matrix):
    n, m = len(matrix), len(matrix[0])
    trails = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                trails += bfs(matrix, i, j, n, m)
    return trails


def bfs(matrix, i, j, n, m):
    complete_trails = 0
    seen = set()
    q = deque([(i, j)])
    while q:
        curr = q.popleft()
        i, j = curr
        # found end
        if matrix[i][j] == 9:
            complete_trails += 1
            continue
        seen.add(curr)  # part 2
        height = matrix[i][j]
        for x, y in directions:
            ni, nj = i + x, j + y
            if ni >= 0 and ni < n and nj >= 0 and nj < m and (ni, nj) not in seen:
                if matrix[ni][nj] == height + 1:
                    # seen.add((ni, nj))  # part 1
                    q.append((ni, nj))
    return complete_trails


if __name__ == "__main__":
    with open("Day 10/input.txt") as file:
        data = file.read().splitlines()
    # data = test_data.splitlines()
    n, m = len(data), len(data[0])
    matrix = [[10] * m for _ in range(n)]
    for i, line in enumerate(data):
        for j in range(m):
            if line[j] != ".":
                matrix[i][j] = int(line[j])
    print(process_trails(matrix))
