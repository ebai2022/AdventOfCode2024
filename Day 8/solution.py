from collections import defaultdict

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def find_antinodes(matrix, antennas):
    antinodes = set()
    for antenna in antennas:
        positions = antennas[antenna]
        # go through each pairing
        for i in range(len(positions)):
            # add the current antenna (part 2)
            antinodes.add(tuple(positions[i]))
            for j in range(i + 1, len(positions)):
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                # bottom side (if -> while for part 2)
                ni = positions[i][0] - dx
                nj = positions[i][1] - dy
                while is_valid(matrix, ni, nj):
                    antinodes.add((ni, nj))
                    ni -= dx
                    nj -= dy
                # top side (if -> while for part 2)
                ni = positions[j][0] + dx
                nj = positions[j][1] + dy
                while is_valid(matrix, ni, nj):
                    antinodes.add((ni, nj))
                    ni += dx
                    nj += dy
    return len(antinodes)


def is_valid(matrix, row, col):
    n, m = len(matrix), len(matrix[0])
    if row >= 0 and row < n and col >= 0 and col < m:
        return True
    return False


if __name__ == "__main__":
    with open("Day 8/input.txt") as file:
        data = file.read().splitlines()
    n, m = len(data), len(data[0])
    matrix = [["."] * m for _ in range(n)]
    antennas = defaultdict(list)
    for i, line in enumerate(data):
        for j in range(m):
            matrix[i][j] = line[j]
            if matrix[i][j] != ".":
                antennas[matrix[i][j]].append([i, j])
    print(find_antinodes(matrix, antennas))
