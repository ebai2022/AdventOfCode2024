from collections import defaultdict


def solution_part1():
    # Read the input file
    with open("Day 1/input.txt", "r") as file:
        data = file.read().splitlines()
    left_arr = []
    right_arr = []
    for line in data:
        nums = line.split()
        left_num, right_num = int(nums[0]), int(nums[1])
        left_arr.append(left_num)
        right_arr.append(right_num)
    left_arr.sort()
    right_arr.sort()
    ans = sum(abs(b - a) for a, b in zip(left_arr, right_arr))
    return ans


def solution_part2():
    # Read the input file
    with open("Day 1/input.txt", "r") as file:
        data = file.read().splitlines()
    left_arr = []
    right_freq = defaultdict(int)
    for line in data:
        nums = line.split()
        left_num, right_num = int(nums[0]), int(nums[1])
        left_arr.append(left_num)
        right_freq[right_num] += 1
    ans = 0
    for left_num in left_arr:
        ans += right_freq[left_num] * left_num
    return ans


if __name__ == "__main__":
    ans = solution_part1()
    print(f"part 1 solution: {ans}")
    ans = solution_part2()
    print(f"part 2 solution: {ans}")
