
# 88. Merge Sorted Array

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    # nums1[:] = nums1[:m]

    count = 0
    # remove the values > m from nums1
    while nums1 and nums1[-1] == 0 and len(nums1) > m:
        count += 1
        nums1.pop()

    nums1.extend(nums2)
    nums1.sort()


# Don't use built-in sort
# Time: O(n + m), Space: O(1)
def merge1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # we work backwards, filling in nums1 from right to left
    # use two pointers, keep track of current index of nums1, nums2
    p1 = m - 1  # pointer to nums1 (excluding zeros)
    p2 = n - 1  # pointer to nums2
    p = len(nums1) - 1  # pointer to next position in nums1, where next element is placed

    # continue until all elements from nums2 are placed in nums1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2 = [2, 5, 6]
    n1 = 3
    merge1(nums1, m1, nums2, n1)
    print(nums1)

    # nums1 = [1, 2, 3, 0, 0, 0]
    # m1 = 3
    # nums2 = [2, 5, 6]
    # n1 = 3
    # merge(nums1, m1, nums2, n1)
    # print(nums1)
    #
    # nums1 = [0]
    # m1 = 0
    # nums2 = [1]
    # n1 = 1
    # merge(nums1, m1, nums2, n1)
    # print(nums1)
    #
    # nums1 = [-1, -1, 0, 0, 0, 0]
    # m1 = 4
    # nums2 = [-1, 0]
    # n1 = 2
    # merge(nums1, m1, nums2, n1)
    # print(nums1)
