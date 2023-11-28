# sample file using bitwise XOR
# binary: base-2 number system
# 2**0, 2**1, 2**2, 2**3, 2**4
#   1 ,   2,   4,     8,    16


def xor_basics():
    a = 5
    b = 3

    # Performing bitwise XOR
    # numbers are converted to their binary representations
    # 5 = 101 in binary
    # 3 = 011 in binary
    # Next the XOR operation is performed on each pair of bits (XOR yields 1 if bits are different, 0 if same)
    result = a ^ b
    # Starting from the RIGHT
    # First bit   1 ^ 1 = 0
    # Second bit  0 ^ 1 = 1
    # Third bit   1 ^ 0 = 1
    # resulting bits are compiled into binary 110, 6 in decimal
    # The rightmost bit represents 2**0 (which equals 1), when the bit is set
    # The second bit from the right represents 2**1 (which equals 2), when set
    # The third bit from the right represents 2**2 (which equals 4), when set

    # first bit 2**0 = 1, bit set to 0 so,  0 * 1 = 0
    # second bit 2**1 = 2, bit set to 1 so,  1 * 2 = 2
    # third bit 2**2 = 4, bit set to 1 so,   1 * 4 = 4
    # 2 + 4 = 6

    # Show the binary representation
    # [2:] used to skip the first two characters of the string, which are 0b
    # it makes sense to remove the 0b in this context to focus on the binary digits themselves
    # if you're storing or using the binary representation programmatically, you might keep the 0b
    # to maintain clarity that the string represents a binary number.
    binary_a = bin(a)[2:]
    binary_b = bin(b)[2:]
    binary_result = bin(result)[2:]

    print(f' Binary of 5: {binary_a}')
    print(f' Binary of 3: {binary_b}')
    print(f' Binary result of 5 ^ 3: {binary_result}')
    print(f' Decimal result of 5 ^ 3: {result}')


def xor_data_masking(char, key):
    """
    Data is masked (or encrypted) by XORing it with a key
    Same key is used to unmask(or decrypt) the data
    """

    # Let's consider a simple single character
    # We encrypted 'A' using an XOR operation with the key '123'. The encrypted(masked) value is '58'
    # When we decrypted(unmasked) this value using the same key, returned the orginal character 'A'

    # Convert to ASCII
    ascii_value = ord(char)

    #XOR the ASCII value with the key
    masked_value = ascii_value ^ key

    # To decrypt, XOR the masked value with the same key
    original_value = masked_value ^ key
    decrypted_char = chr(original_value)

    return masked_value, decrypted_char


if __name__ == '__main__':
    xor_basics()

    char_to_encrypt = 'A'
    encryption_key = 123 # Arbitrary key

    masked, decrypted = xor_data_masking(char_to_encrypt, encryption_key)
    print(f"Masked Value, {masked}")
    print(f"Decrypted Character, {decrypted}")
