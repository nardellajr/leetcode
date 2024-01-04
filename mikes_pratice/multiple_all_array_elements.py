# Create a method that multiplies each element of the array
# to each element of the array
# [2,3,4]  = 2 * 2, 2 * 3, 2 * 4, 3 * 2, 3 * 3, 3 * 4, 4 * 2, 4 * 3, 4 * 4 = 81

# Time complexity is O(n**2)
def cal_each_element(arr):
    grand_total = 0
    for i in arr:
        for j in arr:
            grand_total += i * j

    return grand_total


# Same Time complexity as above O(n**2)
def recursive_cal(arr, start=0, total=0):
    # base case
    if start == len(arr):
        return total

    for j in range(len(arr)):
        total += arr[start] * arr[j]

    return recursive_cal(arr, start + 1, total)




if __name__ == '__main__':
    arr = [2, 3, 7, 8, 10]
    # arr = [2, 3]
    print(cal_each_element(arr))

    arr = [2, 3, 4]
    print(recursive_cal(arr))
