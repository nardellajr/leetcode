
# 2859. Sum of values at indices With k set bits

# Return an integer that denotes the sum of elements in nums whose corresponding
# indices have exactly k set bits in their binary representation.

# The set bits in an integer are the 1's present when it is written in binary.
# For example, the binary representation of 21 is 10101, which has 3 set bits

def sumIndicesWithKSetBits(nums, k):
    # count if binary contains k set bits
    total = 0
    # loop through the indices
    for j in range(len(nums)):
        # print('bin count: ', bin(j).count('1'))
        if bin(j).count('1') == k:
            total += nums[j]

    return total


if __name__ == '__main__':
    nums = [5,10,1,5,2]
    k = 1
    print(sumIndicesWithKSetBits(nums, k))

    nums = [4, 3, 2, 1]
    k = 2
    print(sumIndicesWithKSetBits(nums, k))



# convert each indices to binary
# indices_binary = [bin(i) for i in range(len(nums))]
# print(indices_binary)