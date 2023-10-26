
# 26. Remove Duplicates from Sorted Array

# Brute Force, Time: O(n), Space: O(n)
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 1:
        return 1

    # start from end of array
    for i in range(len(nums) - 1, -1, -1):
        # if duplicate, remove it
        if nums[i] == nums[i - 1]:
            nums.remove(nums[i])

        if len(nums) == 1:
            break

    return len(nums)


# Use Dictionary
def removeDuplicates1(nums: list[int]) -> int:
    current_elements = {}
    for i in range(len(nums) - 1, -1, -1):
        # add to dictionary if not already in it
        if nums[i] not in current_elements.values():
            current_elements[i] = nums[i]
        else:
            # if duplicate, remove it
            nums.pop(i)

    return len(current_elements.keys())


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
    print(nums)
    nums = [1, 1, 2]
    print(removeDuplicates1(nums))
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums))
    print(nums)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates1(nums))
    print(nums)

    nums = [1]
    print(removeDuplicates(nums))
    print(nums)
    nums = [1]
    print(removeDuplicates1(nums))
    print(nums)

    nums = [1, 1]
    print(removeDuplicates(nums))
    print(nums)
    nums = [1, 1]
    print(removeDuplicates1(nums))
    print(nums)
