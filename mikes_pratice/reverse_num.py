
# Methods to reverse numbers

# Mathematical Manipulation
def reverse_number(num):
    reversed_num = 0

    while num > 0:
        # gets remainder of the division of num by 10
        # 12345/10 = 1234.5
        digit = num % 10  # Get the last digit

        # multiplying by 10 always adds a zero at the end of the number
        # Say reversed_num = 5 * 10 = 50, then adding digit would be placed in the rightmost position
        reversed_num = reversed_num * 10 + digit  # Append digit to reversed number

        # floor division, keep whole number pare, any fractional part (decimal) is discarded
        # shift all digits of num to the right by one position
        # num will become 0, which exits the loop
        num //= 10  # Remove last digit

    return reversed_num


def reversed_num2(num):
    reversed_number = int(str(num)[::-1])
    return reversed_number


def rev(x):
    rx = 0

    while x > 0:
        rx *= 10
        rx += x % 10
        x //= 10

    return rx



if __name__ == '__main__':
    num = 12345
    print(f'original number: {num}, reversed number2: {rev(num)}')
    # reverse_number(num)
    print(f'original number: {num},  reversed number: {reverse_number(num)}')

    print(f'original number: {num}, reversed number2: {reversed_num2(num)}')


