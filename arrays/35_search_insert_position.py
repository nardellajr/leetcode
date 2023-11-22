# Binary Search
# Efficient for Searching Sorted array or list.

# If Array isn't sorted here are a couple of other approaches:

# Linear Search - loop thru each element O(n)
# Hashing - if search multiple times, store Array elements in python dictionary, which allows for faster lookups
#  O(1), but requires additional space

# Time O(log n)
# Space O(1)
def binary_search(arr: list[int], target: int) -> int:
    """
    Input Array must be Sorted
    Returns index of target, else -1
    """

    # Initial Boundaries
    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot = (low + high) // 2

        if arr[pivot] < target:
            low = pivot + 1
        elif arr[pivot] > target:
            high = pivot - 1
        else:
            return pivot

    return low # target not found, index where it should be



if __name__ == '__main__':
    arr = [1,3,5,6]
    target = 2
    result = binary_search(arr, target)
    print('Not found: ', result)

    arr = [1, 3, 5, 7, 9, 11]
    target = 3
    result = binary_search(arr, target)
    print("Index of target:", result)


    arr = [1, 3, 5, 7, 9, 11]
    target = 8
    result = binary_search(arr, target)
    print("Not Found:", result)

