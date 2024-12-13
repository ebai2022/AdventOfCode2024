import re

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


if __name__ == "__main__":
    with open("Day 13/input.txt") as file:
        data = file.read().splitlines()
    # data = test_data.splitlines()
    tokens = 0
    num_found = 0
    for line in data:
        if line.startswith("Button A:"):
            match = re.search(r"X\+(\d+), Y\+(\d+)", line)
            ax, ay = int(match.group(1)), int(match.group(2))
        elif line.startswith("Button B:"):
            match = re.search(r"X\+(\d+), Y\+(\d+)", line)
            bx, by = int(match.group(1)), int(match.group(2))
        elif line.startswith("Prize"):
            match = re.search(r"X=(\d+), Y=(\d+)", line)
            # add 10000000000000 for part 2, remove for part 1
            px, py = int(match.group(1)) + 10000000000000, int(match.group(2)) + 10000000000000
            b = (py * ax - ay * px) / (ax * by - ay * bx)
            a = (py * bx - px * by) / (ay * bx - ax * by)
            if int(a) == a and int(b) == b:
                tokens += int(a) * 3 + int(b)
                num_found += 1
    print(tokens, num_found)


"""
ax * a + bx * b = px
ay * a + by * b = py

Solve!

x1 * a + y1 * b = z1
x2 * a + y2 * b = z2
a = (z1 - y1 * b) / x1

x2 * (z1 - y1 * b) / x1 + y2 * b = z2

(x2 * z1 - x2 * y1 * b) / x1 + y2 * b = z2

x2 * z1 - x2 * y1 * b + x1 * y2 * b = z2 * x1

b * (x1 * y2 - x2 * y1) = z2 * x1 - x2 * z1
b = (z2 * x1 - x2 * z1) / (x1 * y2 - x2 * y1)

b = (py * ax - ay * px) / (ax * by - ay * bx)
################################################
b = (z1 - x1 * a) / y1
x2 * a + y2 * (z1 - x1 * a) / y1 = z2
x2 * a * y1 + y2 * z1 - y2 * x1 * a = z2 * y1
a * (x2 * y1 - x1 * y2) = z2 * y1 - z1 * y2
a = (z2 * y1 - z1 * y2) / (x2 * y1 - x1 * y2)

a = (py * bx - px * by) / (ay * bx - ax * by)
"""