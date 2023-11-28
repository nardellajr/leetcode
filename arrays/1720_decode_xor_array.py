# 1720 Decode XORed Array

# There is a hidden integer array arr that consists of n non-negative integers.

# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].

def decode(encoded: list[int], first: int) -> list[int]:
    decoded = [first]
    for i in range(len(encoded)):
        decoded.append(decoded[i] ^ encoded[i])
    return decoded

# Time O(n)
# Space O(1)
def decode2(encoded: list[int], first: int) -> list[int]:
    # encoded is the key
    # Initialize the array with the first element
    arr = [first]

    # Iterate through the encoded (key) array
    for num in encoded:
        # arr[-1] gets the last element in arr, then we do XOR with each encoded (key) element
        # first time in loop, arr[-1] is 1 and first item in encoded was 1, 1 ^ 1
        # converted to binary 2**0 = 1, bit is set so 1 * 1 = 1
        # convert the other 1 to binary 2**0 = 1, bit is set so 1 * 1 = 1
        # 1 XOR 1 = 0, 0 is appended to arr
        # Now arr[-1] is 0 and num 2
        # 2**0 = 1, bit not set, 0 * 1 = 0, num 2 = 2**0 = 1, bit no set 0 * 1 = 0, 2**1 = 2, bit set 1 * 2 = 2
        # aligned by their rightmost bit, pad with leading zeroes, binary representation 00 ^ 10
        # First bit 0 ^ 0 = 0
        # Second bit 0 ^ 1 = 1
        # result is binary 10, is 2 in decimal, which is appended to arr
        arr.append(arr[-1] ^ num)

    return arr


if __name__ == '__main__':
    encoded_example = [1, 2, 3]
    first_example = 1

    print(f"decode: {decode(encoded_example, first_example)}")
    print(f"decode2: {decode2(encoded_example, first_example)}")

    encoded_example = [6, 2, 7, 3]
    first_example = 4
    print(f"decode: {decode(encoded_example, first_example)}")
    print(f"decode2: {decode2(encoded_example, first_example)}")



