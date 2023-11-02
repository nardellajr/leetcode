# 169. Majority Element
# Difficulty: Easy

# Given an array of size n, find the majority element. The majority element is the element that appears more than
# ⌊n / 2⌋ times. You may assume that the array is non-empty and the majority element always exist in the array.

# Space: O(n), since we create dictionary to store elements, and worst case is that all elements are unique
# Time: O(n), since we iterate through the array, and then iterate through the dictionary O(1)
def majority_element(nums: list[int]) -> int:
    elements = {}
    for i in range(len(nums)):
        if nums[i] not in elements.keys():
            elements[nums[i]] = 1
        else:
            elements[nums[i]] += 1

    return max(elements, key=elements.get)


# Space: O(1), since we only store the current candidate and count
# Time: O(n), since we iterate through the array once
def majority_element1(nums: list[int]) -> int:
    curr_candidate = nums[0]
    count = 1
    for i in range(1, len(nums)):
        # update candidate if count is 0
        if count == 0:
            curr_candidate = nums[i]
            count += 1
        elif curr_candidate == nums[i]:
            count += 1
        else:
            count -= 1
    return curr_candidate


if __name__ == '__main__':

    v = [3, 2, 3]
    print(majority_element(v))
    # should return 3
    print(majority_element1(v))

    v = [2,2,1,1,1,2,2]
    print(majority_element(v))
    # should return 2
    print(majority_element1(v))
