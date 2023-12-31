# 1480. Running Sum of 1d Array
import random
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]... nums{i]).
# Return the running sum of nums

import time

# Time O(N^2), Space O(N)
def runningSum(nums: list[int])-> list[int]:
    results = []
    for i in range(len(nums)):
        # print(sum(nums[:i + 1]))
        results.append(sum(nums[:i + 1]))

    return results

# Time O(N^2), Space O(N)
# The for is looping thru N items and sum(nums[:i + 1]) is doing another loop, that is why N^2
def runningSum2(nums: list[int]) -> list[int]:
    return [sum(nums[:i + 1]) for i in range(len(nums))]


# Runs faster than other methods
# Time O(N)
# Space O(N)
def runningSum3(nums: list[int]) -> list[int]:
    runSum = [0] * len(nums)  # pre defining array size does save time when the array gets large
    runSum[0] = nums[0]
    for i in range(1, len(nums)):
        # since we have already calculated total of the previous element, us it
        runSum[i] = runSum[i - 1] + nums[i]
        # this eliminates another loop

    return runSum


def runningSum4(nums: list[int]) -> list[int]:
    runSum = [nums[0]]
    for i in range(1, len(nums)):
        runSum.append(runSum[i - 1] + nums[i])

    return runSum



if __name__ == '__main__':

    nums_list = []
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 1, 1, 1, 1]
    nums3 = [3, 1, 2, 10, 1]

    nums_list.append(nums1)
    nums_list.append(nums2)
    nums_list.append(nums3)

    for n in nums_list:
        print(runningSum(n))

    # This has the fastest runtime, but we are only using small array
    begin = time.perf_counter()
    print(runningSum(nums1))
    print(f'Runtime: ', time.perf_counter() - begin)

    begin = time.perf_counter()
    print(f'runningSum2: ', runningSum2(nums1))
    print(f'Runtime: ', time.perf_counter() - begin)

    begin = time.perf_counter()
    print(f'runningSum3: ', runningSum3(nums1))
    print(f'Runtime: ', time.perf_counter() - begin)

    # This is the second fastest
    begin = time.perf_counter()
    print(f'runningSum4: ', runningSum4(nums1))
    print(f'Runtime: ', time.perf_counter() - begin)


    # large array test
    large_nums = [random.randint(1, 100) for _ in range(2000)]

    begin = time.perf_counter()
    runningSum(large_nums)
    print(f'runningSum - Runtime: ', time.perf_counter() - begin)

    # Fastest as array increases in size
    begin = time.perf_counter()
    runningSum3(large_nums)
    print(f'runningSum3 - Runtime: ', time.perf_counter() - begin)

    begin = time.perf_counter()
    runningSum4(large_nums)
    print(f'runningSum4 - Runtime : ', time.perf_counter() - begin)


