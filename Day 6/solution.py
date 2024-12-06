from collections import defaultdict

# states: upwards (-1, 0), right (0, 1), down (-1, 0), left (0, -1)
states = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_distinct_positions(matrix, start):
    state = 0
    seen = set()
    processed_nodes = defaultdict(set)
    obstacles = set()
    while True:
        i, j = start
        seen.add(start)
        processed_nodes[start].add(state)
        next_start = (i + states[state][0], j + states[state][1])
        if is_valid(matrix, next_start):
            # # try to put an obstacle and create a loop if there is no obstacle already present
            # if (
            #     matrix[next_start[0]][next_start[1]] != "#"
            #     and matrix[next_start[0]][next_start[1]] != "^"
            # ):
            #     # simulate putting an obstacle there
            #     matrix[next_start[0]][next_start[1]] = "#"
            #     if find_possible_loops(matrix, start, state):
            #         obstacles.add((next_start))
            #     matrix[next_start[0]][next_start[1]] = "."
            # # find the next valid direction to explore
            while (
                is_valid(matrix, next_start)
                and matrix[next_start[0]][next_start[1]] == "#"
            ):
                state = (state + 1) % 4
                next_start = (i + states[state][0], j + states[state][1])
            start = next_start
        else:
            break
    return len(seen), len(obstacles)


def find_possible_loops(matrix, start, state):
    n, m = len(matrix), len(matrix[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == ".":
                seen = set()
                curr_state = state
                x, y = start
                # simulate a barrier there
                matrix[i][j] = "#"
                while is_valid(matrix, (x + states[curr_state][0], y + states[curr_state][1])):
                    if matrix[x + states[curr_state][0]][y + states[curr_state][1]] == "#":
                        # change direction
                        curr_state = (curr_state + 1) % 4
                    if (x, y, curr_state) in seen:
                        ans += 1
                        break
                    seen.add((x, y, curr_state))
                    x, y = states[curr_state][0] + x, states[curr_state][1] + y
                matrix[i][j] = "."
    return ans
    # seen = set((start[0], start[1], state))
    # state = (state + 1) % 4
    # while True:
    #     i, j = start
    #     if (i, j, state) in seen:
    #         return True
    #     seen.add((i, j, state))
    #     next_start = (i + states[state][0], j + states[state][1])
    #     if is_valid(matrix, next_start):
    #         while (
    #             is_valid(matrix, next_start)
    #             and matrix[next_start[0]][next_start[1]] == "#"
    #         ):
    #             state = (state + 1) % 4
    #             next_start = (i + states[state][0], j + states[state][1])
    #         start = next_start
    #     else:
    #         return False


def is_valid(matrix, start):
    n, m = len(matrix), len(matrix[0])
    i, j = start
    if i >= 0 and i < n and j >= 0 and j < m:
        return True


if __name__ == "__main__":
    with open("Day 6/input.txt", "r") as file:
        data = file.read().splitlines()
    n, m = len(data), len(data[0])
    matrix = [["."] * m for _ in range(n)]
    row = 0
    for line in data:
        for i in range(m):
            matrix[row][i] = line[i]
            if line[i] == "^":
                start = (row, i)
        row += 1
    print(start)
    print(find_distinct_positions(matrix, start))
    print(find_possible_loops(matrix, start, 0))