# 1389. Create Target Array in the Given Order

# nums list is the input values
# index list is the location of nums[index] in the target list

import time

def create_target_array(nums: list[int], index: list[int]) -> list[int]:
    nums_length = len(nums)
    target_array = [None] * nums_length
    for c, i in enumerate(index):
        value =  nums[c]
        if target_array[i] is not None:
            for x in range(nums_length - 1, i, -1):
                target_array[x] = target_array[x - 1]

        target_array[i] = value

    return target_array


def create_target_array2(nums: list[int], index: list[int]) -> list[int]:
    # can use slice notation to insert into a list

    target = [None] * len(nums)
    for i in range(len(nums)):
        if target[index[i]] is not None:
            # get the values from the index to the end of the list
            # and insert them into the list starting at index + 1
            target[index[i] + 1:] = target[index[i]:-1]

        target[index[i]] = nums[i]

    return target


def create_target_array3(nums: list[int], index: list[int]) -> list[int]:
    # use zip
    target = []
    # Returns an interator of tuples, where the i-th tuple contains the i-th element from each of the lists
    # (nums, index) = [(0, 0), (1, 1), (2, 2), (3, 2), (4, 1)]
    for n, i in zip(nums, index):
        # insert n into the target list at index i
        target[i:i] = [n]

    return target



if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]

    begin = time.perf_counter()
    r = create_target_array(nums, index)
    print(f"time: ", time.perf_counter() - begin)
    print(f'results: {r}')

    begin = time.perf_counter()
    r2 = create_target_array2(nums, index)
    print(f"time2: ", time.perf_counter() - begin)
    print(f'results2: {r2}')

    begin = time.perf_counter()
    r3 = create_target_array3(nums, index)
    print(f"time3: ", time.perf_counter() - begin)
    print(f'results3: {r3}')

