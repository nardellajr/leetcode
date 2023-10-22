import time


# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target
def twoSum(nums: list[int], target: int) -> list[int]:
    # equals 4
    l = len(nums)

    begin = time.perf_counter()
    # Brute Force method
    # values 0 - 3, which is 4 elements
    # First loop runs at O(n), second loop runs at O(n-1)
    # simplifies to O(n**2) time complexity
    for i in range(l):
        for j in range(i + 1, l, 1):
            if (nums[i] + nums[j]) == target:
                print(f'time:', time.perf_counter() - begin)
                return [i, j]


def twoSum_hashmap(nums: list[int], target: int) -> list[int]:
    # More efficient method, using a hashmap (dictionary)
    # hashmap O(1) for lookup, insertion, deletion
    # First loop runs at O(n), then insertion or lookup runs at O(1)
    # simplifies to O(n)
    begin = time.perf_counter()
    numdic = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in numdic:
            print(f'hashmap time: ', time.perf_counter() - begin)
            return [numdic[diff], i]
        else:
            # add to Dictionary (hashmap)
            numdic[n] = i


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Given Target: ", target1, "  Results: ", twoSum(nums1, target1))
    print(f"hashmap Given Target: ", target1, "  Results: ", twoSum_hashmap(nums1, target1))

    print()

    nums1 = [3, 2, 4]
    target1 = 6
    print(f"Given Target: ", target1, "  Results: ", twoSum(nums1, target1))
    print(f"hashmap Given Target: ", target1, "  Results: ", twoSum_hashmap(nums1, target1))

    print()

    nums1 = [3, 3]
    target1 = 6
    print(f"Given Target: ", target1, "  Results: ", twoSum(nums1, target1))
    print(f"hashmap Given Target: ", target1, "  Results: ", twoSum_hashmap(nums1, target1))
