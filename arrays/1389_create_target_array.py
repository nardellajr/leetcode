# 1389. Create Target Array in the Given Order

# nums list is the input values
# index list is the location of nums[index] in the target list

def create_target_array(nums: list[int], index: list[int]) -> list[int]:
    nums_length = len(nums)
    hold_array = []
    target_array = [0] * nums_length
    for x in range(nums_length):
        i = index[x]
        target_array[i] = nums[x]

    return target_array


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]

    r = create_target_array(nums, index)
    print(f'results: {r}')

