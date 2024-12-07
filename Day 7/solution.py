from collections import defaultdict

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def compute_sums_first(arr, index, operation, total, target):
    if index >= len(arr):
        if total == target:
            return total
        else:
            return 0
    if operation == "x":
        total *= arr[index]
    else:
        total += arr[index]
    return max(
        compute_sums_first(arr, index + 1, "x", total, target),
        compute_sums_first(arr, index + 1, "+", total, target),
    )


def compute_sums_second(arr, index, operation, total, target):
    if index >= len(arr):
        if total == target:
            return total
        else:
            return 0
    if operation == "x":
        total *= int(arr[index])
    elif operation == "+":
        total += int(arr[index])
    else:
        # do the "or" operator
        total = int(str(total) + arr[index])
    return max(
        compute_sums_second(arr, index + 1, "x", total, target),
        compute_sums_second(arr, index + 1, "+", total, target),
        compute_sums_second(arr, index + 1, "||", total, target),
    )


if __name__ == "__main__":
    with open("Day 7/input.txt") as file:
        data = file.read().splitlines()
    # data = test_data.splitlines()
    calibrations = defaultdict(list)
    string_calibrations = defaultdict(list)
    for line in data:
        total, nums = line.split(":")
        nums = nums.strip().split()
        int_nums = []
        for num in nums:
            int_nums.append(int(num))
        calibrations[int(total)].append(int_nums)
        string_calibrations[int(total)].append(nums)
    result = 0
    # part 1
    for target in calibrations:
        for operations in calibrations[target]:
            if compute_sums_first(operations, 0, "+", 0, target) > 0:
                result += target
    print(f"part 1 result: {result}")
    # part 2
    result = 0
    for target in string_calibrations:
        for operations in string_calibrations[target]:
            if compute_sums_second(operations, 0, "+", 0, target) > 0:
                result += target
    print(f"part 2 result: {result}")
