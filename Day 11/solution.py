test_data = """125 17"""
MAGIC_NUMBER = 2024


def blink(stone, num_blinks, seen):
    if num_blinks == 75:
        return 1
    key = stone + "|" + str(num_blinks)
    if key in seen:
        return seen[key]
    int_num = int(stone)
    length = len(stone)
    if int_num == 0:
        seen[key] = blink("1", num_blinks + 1, seen)
    elif length % 2 == 0:
        left, right = str(int(stone[: length // 2])), str(int(stone[length // 2 :]))
        seen[key] = blink(left, num_blinks + 1, seen) + blink(right, num_blinks + 1, seen)
    else:
        seen[key] = blink(str(int_num * MAGIC_NUMBER), num_blinks + 1, seen)
    return seen[key]


if __name__ == "__main__":
    with open("Day 11/input.txt") as file:
        stones = file.read().split()
    total = 0
    seen = {}
    for stone in stones:
        total += blink(stone, 0, seen)
    print(total)
