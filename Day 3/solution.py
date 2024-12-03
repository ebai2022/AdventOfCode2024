import re


def part1():
    with open("Day 3/input.txt", "r") as file:
        data = file.read()
    data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = 0
    index = 0
    while index < len(data):
        print(f"data {data[index:]}")
        x = re.search("^mul\(\d*,\d*\)", data[index:])
        if x:
            index += x.end() - 1
            nums = x.group()[4:-1].split(",")
            result += int(nums[0]) * int(nums[1])
        index += 1
    return result


def part2():
    with open("Day 3/input.txt", "r") as file:
        data = file.read()
    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = 0
    index = 0
    enabled = True
    while index < len(data):
        curr = data[index:]
        if curr.startswith("do()"):
            enabled = True
        elif curr.startswith("don't()"):
            enabled = False
        x = re.search("^mul\(\d*,\d*\)", curr)
        if x:
            if enabled:
                nums = x.group()[4:-1].split(",")
                result += int(nums[0]) * int(nums[1])
            index += x.end() - 1
        index += 1
    return result


if __name__ == "__main__":
    ans = part1()
    print(f"part 1 answer: {ans}")
    ans = part2()
    print(f"part 2 answer: {ans}")
