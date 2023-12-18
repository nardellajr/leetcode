# 2574 Left and Right sum difference
# Given a 0-indexed integer array nums, find a 0-indexed array answer where:
# answer.length == nums.length
# answer[i] = [leftSum[i] - rightSum[i]]
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Time complexity: O(n^2)  # calling the sum function 2n times, is the most expensive operation
# Space complexity: O(n)
def left_right_difference(nums: list[int]) -> list[int]:
    left_pointer = 0
    nums_length = len(nums)
    right_pointer = nums_length - 1

    left_sum = []
    right_sum = []
    results = []

    while left_pointer < nums_length:
        if left_pointer == 0:
            left_sum.append(0)
        else:
            left_sum.append(sum(nums[:left_pointer]))
            right_sum.append(sum(nums[left_pointer:]))

        left_pointer += 1
        right_pointer -= 1

    right_sum.append(0)  # last element added

    for i in range(len(nums)):
        results.append(abs(left_sum[i] - right_sum[i]))

    print(f'left_sum: {left_sum}')
    print(f'right_sum: {right_sum}')
    return results


# Time complexity O(n), we are doing 2 loops, but each loop only has O(n)
# Space complexity O(n)
def left_right_differences2(nums: list[int]) -> list[int]:
    # lets sum left elements
    results = []
    nums_length = len(nums)
    # make cum_sum 1 larger than nums, so we can start with 0 and include all element calculations
    cum_sum = [0] * (nums_length + 1)

    for i in range(nums_length):  # 0 - 3
        cum_sum[i + 1] = cum_sum[i] + nums[i]

    print(cum_sum)

    for i in range(nums_length):
        l_sum = cum_sum[i]
        r_sum = cum_sum[nums_length] - cum_sum[i + 1]
        results.append(abs(l_sum - r_sum))

    return results


if __name__ == '__main__':
    nums = [10, 4, 8, 3]
    r2 = left_right_differences2(nums)
    print(f' results2: {r2}')
    r = left_right_difference(nums)
    print(f' results: {r}')

