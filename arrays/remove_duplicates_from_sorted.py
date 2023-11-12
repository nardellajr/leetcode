# 26. Remove Duplicates from Sorted Array

# Code not returning correct results:
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
# unique element appears at most twice. The relative order of the elements should be kept the same.
# For the first test case, I'm returning [1, 2, 3], but it should be [1, 1, 2, 2, 3]

# Brute Force
# Time: O(n), loop thru array once
# Space: O(1), no extra space used
def removeDuplicates(nums: list[int]) -> int:
    """
    list has to be sorted, for this code to work
    """
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
# Time: O(n), loop thru array once
# Space: O(n), create dictionary to store elements, worst case is that all elements are unique
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
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates(nums))
    print(nums)
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates1(nums))
    print(nums)

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
