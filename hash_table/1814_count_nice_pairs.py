# 1814 Count Nice Pairs in Array
import collections


# The numbers in the array need to satisfy the following conditions:
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Take 1 number and the reverse of another number, which equals,
# the second number non-reversed and reversed first number

# Example:
# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.


def countNicePairs(nums: list[int]) -> int:
    # Since that number can be too large, return it modulo 10^9 + 7.
    MOD = 10**9 + 7

    def reversed_num(num):
        rev_num = int(str(num)[::-1])
        return rev_num

    total = 0
    seen = collections.Counter()
    for x in nums:
        f = x - reversed_num(x)
        total += seen[f]
        total %= MOD

        seen[f] += 1

    return total % MOD


if __name__ == '__main__':
    nums = [42,11,1,97]
    print(countNicePairs(nums))
