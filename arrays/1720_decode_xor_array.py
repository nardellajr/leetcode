# 1720 Decode XORed Array

# There is a hidden integer array arr that consists of n non-negative integers.

# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].

def decode(encoded: list[int], first: int) -> list[int]:
    decoded = [first]
    for i in range(len(encoded)):
        decoded.append(encoded[i] ^ decoded[i])
    return decoded


def decode2(encoded: list[int], first: int) -> list[int]:
    # Initialize the array with the first element
    arr = [first]

    # Iterate through the encoded array
    for num in encoded:
        # The next element in arr is the XOR of the last element in arr and the current element in encoded
        arr.append(arr[-1] ^ num)

        return arr


if __name__ == '__main__':
    encoded_example = [1, 2, 3]
    first_example = 1

    print(decode(encoded_example, first_example))
    # print(decode([6, 2, 7, 3], 4))

    decoded_array = decode2(encoded_example, first_example)
    print(decoded_array)


