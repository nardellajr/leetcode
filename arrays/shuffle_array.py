
# 1470 Shuffle the Array

# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].

def shuffle(nums: list[int], n: int) -> list[int]:
    """
    Given the array nums consisting of 2n elements in the form
    [x1,x2,...,xn,y1,y2,...,yn].
    """
    shuffled = []
    for i in range(n):
        shuffled.append(nums[i])
        shuffled.append(nums[i + n])

    return shuffled

def shuffle2(nums: list[int], n: int) -> list[int]:
    """
    Given the array nums consisting of 2n elements in the form
    [x1,x2,...,xn,y1,y2,...,yn].
    """
    shuffled = []
    for i in range(n):
        shuffled.extend([nums[i], nums[i + n]])

    return shuffled


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))