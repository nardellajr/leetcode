# 2824 Count Pairs Whose Sum is Less than Target
# Easy
# Given an array of integers nums and an integer target,
# return the number of pairs i, j where 0 <= i < j < nums.length and nums[i] + nums[j] < target.

def count_pairs(nums: list[int], target: int) -> int:
    matching_pairs = 0
    for index_1 in range(len(nums)):

        item1_val = nums[index_1]
        for index_2 in range(1, len(nums), 1):
            item2_val = nums[index_2]
            print(f'Indexes: {index_1, index_2}')

            if index_1 < index_2:
                if item1_val + item2_val < target:
                    matching_pairs += 1
                    print(f'Indexes matching pair and value: {(index_1, index_2)}, "value: {item1_val + item2_val} "')

    return matching_pairs


def count_pairs1(nums: list[int], target: int) -> int:
    """
     uses two pointers, we only loop thru the list a single time
    """
    counter = 0
    left, right = 0, len(nums) - 1

    # list has to be sorted
    # time complexity = O(n log n)
    nums.sort()

    # left index is less than right index
    while left < right:
        # add values from left most and right most
        if nums[left] + nums[right] < target:
            # if len of list was 10, 10 - 0 = 10
            counter += right - left
            # move left pointer towards the right pointer
            left += 1
        else:
            # move right point towards the left pointer
            right -= 1

    return counter


if __name__ == '__main__':
    val = [-1, 1, 2, 3, 1]
    target_val = 2
    print(f'Pairs < target: ', count_pairs(val, target_val))
    print(f'Pairs < target: ', count_pairs1(val, target_val))

    val = [-6,2,5,-2,-7,-1,3]
    target_val = -2
    print(f'Pairs < target: ', count_pairs(val, target_val))
    print(f'Pairs < target: ', count_pairs1(val, target_val))
