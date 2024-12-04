def part1(matrix, n, m):
    ans = 0
    # search matrix for "xmas"
    for i in range(n):
        for j in range(m):
            ans += check_XMAS(i, j, n, m, matrix)
    return ans


def part2(matrix, n, m):
    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == "A":
                diag_left = matrix[i - 1][j + 1] + "A" + matrix[i + 1][j - 1]
                diag_right = matrix[i - 1][j - 1] + "A" + matrix[i + 1][j + 1]
                if (diag_left == "MAS" or diag_left == "SAM") and (
                    diag_right == "MAS" or diag_right == "SAM"
                ):
                    ans += 1
    return ans


def check_XMAS(i, j, n, m, matrix):
    ans = 0
    # lower_diag
    lower_diag = ""
    for k in range(4):
        if i + k < n and j + k < m:
            lower_diag += matrix[i + k][j + k]
    ans += lower_diag == "XMAS" or lower_diag == "SAMX"
    # upper diag
    upper_diag = ""
    for k in range(4):
        if i - k >= 0 and j + k < m:
            upper_diag += matrix[i - k][j + k]
    ans += upper_diag == "XMAS" or upper_diag == "SAMX"
    # within the same row
    row = ""
    for k in range(j, min(m, j + 4)):
        row += matrix[i][k]
    ans += row == "XMAS" or row == "SAMX"
    # within the same column
    column = ""
    for k in range(i, min(n, i + 4)):
        column += matrix[k][j]
    # print(f"{required} for start {i, j}")
    ans += column == "XMAS" or column == "SAMX"
    return ans


if __name__ == "__main__":
    # Read input
    with open("Day 4/input.txt", "r") as file:
        data = file.read().splitlines()
    # create matrix
    matrix = []
    for line in data:
        curr_row = []
        for char in line:
            curr_row.append(char)
        matrix.append(curr_row)
    n, m = len(matrix), len(matrix[0])
    ans = part1(matrix, n, m)
    print(ans)
    ans = part2(matrix, n, m)
    print(ans)
