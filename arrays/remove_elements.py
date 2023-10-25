
# 27 Remove Elements
# Time: O(n), Space: O(1)
def removeElement(nums: list[int], val: int) -> int:
    # Remove elements from the end, so it doesn't affect the index
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            # nums.insert(i, -1)
            nums.remove(val)

    return nums


def removeElement1(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)

    return len(nums)


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    n = removeElement(nums, val)
    print(n)
    nums = [3, 2, 2, 3]
    n = removeElement1(nums, val)
    print(n)

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    n = removeElement(nums, val)
    print(n)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    n = removeElement1(nums, val)
    print(n)

    nums = [1]
    val = 1
    n = removeElement(nums, val)
    print(n)
    nums = [1]
    n = removeElement1(nums, val)
    print(n)
