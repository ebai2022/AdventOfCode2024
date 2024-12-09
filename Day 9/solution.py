import copy

test_data = "2333133121414131402"


def uncompress_data(data):
    ans = []
    for i in range(len(data)):
        amount = int(data[i])
        if i % 2 == 0:  # files
            for j in range(amount):
                ans.append(i // 2)
        else:  # free space
            for j in range(amount):
                # -1 represents "."
                ans.append(-1)
    return ans


def move_data(uncompressed_data):
    left = 0
    right = len(uncompressed_data) - 1
    while left < right:
        if uncompressed_data[left] != -1:
            left += 1
            continue
        if uncompressed_data[right] == -1:
            right -= 1
            continue
        # swap left and right
        uncompressed_data[left], uncompressed_data[right] = (
            uncompressed_data[right],
            uncompressed_data[left],
        )


def move_blocks(uncompressed_data):
    left = 0
    right = len(uncompressed_data) - 1
    while left < right:
        # find the next white space on the left and the next non-white space on the right
        if uncompressed_data[left] != -1:
            left += 1
            continue
        if uncompressed_data[right] == -1:
            right -= 1
            continue
        # get the length of the free space
        free_index, num_length = get_next_swappable_index(uncompressed_data, right)
        # no way to swap (no free space block is big enough), move the right pointer
        if free_index == -1:
            right -= num_length
        else:
            for i in range(num_length):
                # swap left and right
                uncompressed_data[free_index + i], uncompressed_data[right] = (
                    uncompressed_data[right],
                    uncompressed_data[free_index + i],
                )
                right -= 1


def get_next_swappable_index(arr, num_index):
    # get num_length
    num_length = 1
    while arr[num_index] == arr[num_index - num_length]:
        num_length += 1
    # find the next free length that can fit this number
    free_length = 0
    for i in range(num_index):
        if free_length >= num_length:
            return i - free_length, num_length
        if arr[i] == -1:
            free_length += 1
        else:
            free_length = 0
    return -1, num_length


def calculate_checksum(arr):
    total = 0
    for i, num in enumerate(arr):
        if num != -1:
            total += i * num
    return total


if __name__ == "__main__":
    # preprocess the data
    with open("Day 9/input.txt") as file:
        data = file.read()
    uncompressed_data = uncompress_data(data)
    # part 1
    ans = copy.deepcopy(uncompressed_data)
    move_data(ans)
    print(f"part 1 answer: {calculate_checksum(ans)}")
    # part 2
    ans = copy.deepcopy(uncompressed_data)
    move_blocks(ans)
    print(f"part 2 answer: {calculate_checksum(ans)}")
