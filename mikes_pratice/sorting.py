
# This is a recursive function

# Worst case Time O(N^2)
def quick_sort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choosing a pivot (here, we're simply choosing the last element as the pivot)
    pivot = arr[len(arr) - 1]

    # Creating two sub-arrays for elements less than and greater than the pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    # The pivot is in its final sorted position, so no need to include it in recursive calls
    # Recursively applying quick_sort to the left and right sub-arrays
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)