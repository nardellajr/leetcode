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

def sum_odd_length_subarray(arr: list[int]) -> int:
    print(f'sum old-length sub-arrays from: {arr}')
    t = 0
    l = len(arr)
    for i in range(l):
        for j in range(i, l, 2):  # step 2, to get odd values
            sub_array = arr[i: j + 1]
            print(sub_array)
            k = sum(sub_array)
            print(f'i: {i}, j + 1: { j + 1}, odd value total: {k}')
            t+= k
    return t

def sum_odd_length_subarray2(arr: list[int]) -> int:
    # The idea is to find the frequency of each element in the array.
    # How many odd-length subarrays can each element be part of?
    # For example, if the array is [1, 4, 2, 5, 3], element arr[0] = 1.
    # The answer is (len(arr)+1)//2. Therefore, the freq of element arr[0] = 1 is (5+1)//2=3.
    # freq = 3 for arr[0] = 1, so we add 3*1 to the result.

    res = 0
    freq = 0
    n = len(arr)
    for i in range(n):
        part1 = (i + 1)// 2
        print(f'part1: {part1}')
        print(f'freq: {freq}')
        part1a = freq - (i + 1)// 2
        part2 = (n - i + 1)// 2
        print(f'part1a: {part1a}, part2: {part2}, added: {part1a + part2}')

        freq = freq - (i + 1)//2 + (n - i + 1)//2
        res += freq * arr[i]

    return res


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    # print(f'test: {sumOddlengthSubarrays(arr)}')

    print(f'working: {sum_odd_length_subarray(arr)}')

    print(f'subarray2 - Uses Frequency: {sum_odd_length_subarray2(arr)}')


# Explanation for sum_odd_length_subarray2
# for example arr = [1,4,2,5,3], element arr[0] = 1. The appearing freq of head element arr[0]
# should be how many odd-length sub arrays it can generate.
# The answer is (len(arr)+1)//2. Therefore, the freq of element arr[0] = 1 is (5+1)//2=3.

# Now let's take element arr[1] = 4 for example, if we take element arr[0] = 1 out,
# then arr[1] = 4 becomes the new head element, thus the freq of arr[1] = 4 in the
# new subarray could be calculated as the same way of arr[0] = 1.
# It seems that all we need to do is add the freq of previous element arr[0] up then we get the freq of arr[1].

# No, we also need to minus the subarrays of previous element arr[0] = 1 when they
# do not include arr[1]=4. In this case, it is [1]. This is why freq[i] = freq[i-1]-(i+1)//2+(n-i+1)//2.

