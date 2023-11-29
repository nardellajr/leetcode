# 1588 Sum of all Odd length Subarrays

# return sum of all possible odd-length subarrays

def sumOddlengthSubarrays(arr: list[int]) -> int:
    arr_dict = {}
    for n in range(len(arr)):
        if n % 2 == 0:
            print(f'Even: {n}')
        else:
            print(f'Odd: {n}')
            # based on Odd index, that is the number of elements we need to add
    return 99

def sum_odd_length_subarray(arr: list[int]) -> int:
    t = 0
    l = len(arr)
    for i in range(l):
        for j in range(i, l, 2):  # step 2, to get odd values
            t += sum(arr[i:j + 1])
    return t

if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(f'test: {sumOddlengthSubarrays(arr)}')

    print(f'working: {sum_odd_length_subarray(arr)}')



