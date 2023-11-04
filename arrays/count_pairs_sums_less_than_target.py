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

            if item1_val + item2_val < target:
                matching_pairs += 1
                print(f'Indexes matching pair and value: {(index_1, index_2)}, "value: {item1_val + item2_val} "')

    return matching_pairs


if __name__ == '__main__':
    val = [-1, 1, 2, 3, 1]
    target_val = 2
    print(f'Pairs < target: ', count_pairs(val, target_val))

    val = [-6,2,5,-2,-7,-1,3]
    target_val = -2
    print(f'Pairs < target: ', count_pairs(val, target_val))

