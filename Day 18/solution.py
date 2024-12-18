from collections import deque
test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(matrix, start, end):
    queue = deque([start])
    visited = set()
    num_steps = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            x, y = queue.popleft()
            if (x, y) == end:
                print("found the end")
                return True
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == 0:
                    queue.append((nx, ny))
        num_steps += 1
    return False

if __name__ == "__main__":
    with open("Day 18/input.txt") as file:
        data = file.read().splitlines()
    # data = test_data.splitlines()
    matrix = [[0] * 71 for _ in range(71)]
    for line in data[:2900]:
        x, y = line.split(",")
        matrix[int(y)][int(x)] = 1
    for i in range(2800, 2930):
        x, y = data[i].split(",")
        matrix[int(y)][int(x)] = 1
        if not (bfs(matrix, (0, 0), (70, 70))):
            print(i)
            print(data[i])
            break