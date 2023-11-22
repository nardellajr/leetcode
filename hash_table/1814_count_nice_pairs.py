# 1814 Count Nice Pairs in Array
import collections
import time

# The numbers in the array need to satisfy the following conditions:
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Take 1 number and the reverse of another number, which equals,
# the second number non-reversed and reversed first number

# This could also be nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])
# Doing this nums[i] - rev(nums[i]) returns a number, which can be saved in a hash map
# loop thru the nums adding to the similar values

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
        # Mathematical manipulation
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


# time O(d * n)
def countNicePairs2(nums: list[int]) -> int:
    # MOD = 10**9 + 7
    count = {}
    total = 0

    for n in nums:
        # reverse the string O(d), where d = number of digits in string, d equivalent to n
        # slicing iterates over each character
        rev = int(str(n)[::-1])

        # hash map lookup
        diff_val_count = count.get(n - rev, 0)  # get n - reverse(x) value, else default 0
        total += diff_val_count

        # save in hash map, can't do += to set value
        count[n - rev] = 1 + diff_val_count

    return total % (1000000000 + 7)  # faster than declaring MOD


def countNicePairs3(nums: list[int]) -> int:
    res, d = 0, collections.defaultdict(int)
    for i, n in enumerate(nums):
        k = n - int(str(n)[::-1])
        res += d[k]
        d[k] += 1
    return res % (10**9 + 7)



if __name__ == '__main__':
    nums = [42,11,1,97]

    begin = time.perf_counter()
    print(countNicePairs(nums))
    print('time: ', begin - time.perf_counter())

    # Fastest Method
    begin = time.perf_counter()
    print(countNicePairs2(nums))
    print('time: ', begin - time.perf_counter())

    begin = time.perf_counter()
    print(countNicePairs3(nums))
    print('time: ', begin - time.perf_counter())

