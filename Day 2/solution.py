import copy


def part1():
    with open("Day 2/input.txt", "r") as file:
        data = file.read().splitlines()
    safe_reports = 0
    for line in data:
        elements = line.split()
        valid_window, increasing_window = True, True
        if int(elements[0]) > int(elements[1]):
            increasing_window = False
        # process the level
        length = len(elements)
        for i in range(1, length):
            # print(f"starting at i = {i} with length {len(elements)} for {elements}")
            curr, prev = int(elements[i]), int(elements[i - 1])
            if (
                increasing_window
                and (curr <= prev or curr > prev + 3)
                or not increasing_window
                and (curr >= prev or curr < prev - 3)
            ):
                valid_window = False
                break
        if valid_window:
            safe_reports += 1
    return safe_reports


def part2():
    with open("Day 2/input.txt", "r") as file:
        data = file.read().splitlines()
    safe_reports = 0
    for line in data:
        arr = line.split()
        safe_reports += is_safe(arr, True)
    return safe_reports


def is_safe(arr, has_damper):
    is_increasing = True if int(arr[0]) < int(arr[1]) else False
    for i in range(1, len(arr)):
        curr, prev = int(arr[i]), int(arr[i - 1])
        if (
            is_increasing
            and (curr <= prev or curr > prev + 3)
            or not is_increasing
            and (curr >= prev or curr < prev - 3)
        ):
            if has_damper:
                first_slice = arr[:i] + arr[i + 1 :]
                second_slice = arr[: i - 1] + arr[i:]
                possible_third = 0
                if i == 2:
                    third_slice = arr[i - 1 :]
                    possible_third = is_safe(third_slice, False)
                return max(
                    is_safe(first_slice, False),
                    is_safe(second_slice, False),
                    possible_third,
                )
            return 0
    return 1


if __name__ == "__main__":
    ans = part1()
    print(ans)
    ans = part2()
    print(ans)
