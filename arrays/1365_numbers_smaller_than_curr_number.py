# 1365 How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]

# Sort Array, then use index to determine numbers smaller

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    '''
    Brute force method
    '''
    output = []
    for i in nums:
        count_item_smaller = 0
        for j in nums:
            if j < i:
                count_item_smaller += 1

        output.append(count_item_smaller)

    return output


def smallerNumbersThanCurrent1(nums: list[int]) -> list[int]:
    copy_nums = list(nums)
    copy_nums.sort()
    # print(copy_nums)
    # print(nums)
    output = []
    for i in nums:
        output.append(copy_nums.index(i))

    return output


if __name__ == '__main__':

    nums1 = [8,1,2,2,3]
    print(smallerNumbersThanCurrent1(nums1))

    nums2 = [6,5,4,8]
    # print(smallerNumbersThanCurrent(nums2))
    print(smallerNumbersThanCurrent1(nums2))
    #
    nums3 = [7,7,7,7]
    # print(smallerNumbersThanCurrent(nums3))
    print(smallerNumbersThanCurrent1(nums3))


