
# brute force method O(n^2) - time, O(1) - space
def numIdenticalPairs(nums: list[int]) -> int:
    good_pair = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                good_pair += 1

    return good_pair


# dictionary method O(n), O(n) - space
def dic_numIdenticalPairs(nums: list[int]) -> int:
    count = {}
    good_pair = 0
    for num in nums:
        # if num in dictionary, add the value of the key to good_pair
        if num in count:
            good_pair += count[num]
            # increment the value of the key
            count[num] += 1
        else:
            count[num] = 1

    return good_pair


if __name__ == '__main__':
    # nums = [1, 2, 3, 1, 1, 3]
    nums = [1, 1, 1, 1]
    print(numIdenticalPairs(nums))

    print(dic_numIdenticalPairs(nums))



