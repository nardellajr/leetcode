def getConcatenation(nums: list[int]) -> list[int]:
    return nums[:] + nums[:]


# string that reads the same forward as backwards
# We need to find the same letter(s) at the beginning and end of the string, with gap between them
# the gap means it's not the same letter
def countPalindromicSubsequence(s: str) -> int:
    res = 0
    # creates a set with unique values
    # {a, a, b, c, a}
    # {c, a, b}
    unq_str = set(s)
    # print(unq_str)

    # So what is going on here?
    # Going thru the logic
    # Looking at each item in the unq_str {c, a, b}
    # start with c, search from the beginning of s, get position
    # search from the end of s, get position
    for v in unq_str:
        start = s.find(v)  # where is the first occurrence of the letter
        end = s.rfind(v)  # where in the text is the last occurrence of the letter

        # c positions are 3,3: bypass if
        # a positions are 0,4: enter if
        if start < end:
            # s[start + 1: end], get the letters between the common letter a, 'abc'
            # set() gets unique letters, 'abc'
            # len('abc') is 3, letters between the 'a' found at the beginning and end of the s
            # there are 3 possible palindromic combinations
            # 'aaa', 'aba', 'aca'
            res += len(set(s[start+1:end]))

    return res


def get_palindromic_values(s: str) -> list[str]:
    unq_str = set(s)
    pals = list()
    for v in unq_str:
        start = s.find(v)
        end = s.rfind(v)

        if start < end:
            letters_between = set(s[start + 1:end])
            for l in letters_between:
                pal = v + l + v
                pals.append(pal)

    return pals


def get_largest_palindromic(s: str) -> str:
    """
    One bruteforce method
    """
    unique_str = set(s)
    largest_pal = ""
    max_pal = 0
    if len(unique_str) == 1:
        return s
    elif len(unique_str) == len(s):
        return s[0]

    for letter in unique_str:
        start = s.find(letter)
        end = s.rfind(letter)

        if start < end:
            all_letters_between = s[start + 1: end]
            unq_letters_between = set(s[start + 1: end])
            # if all_letters_between is odd, remove the middle letter
            all_len = len(all_letters_between)
            center = all_len // 2
            # if odd length, get the middle letter
            if all_len % 2 != 0:
                middle_letter = all_letters_between[center]
                if middle_letter in unq_letters_between:
                    unq_letters_between.remove(middle_letter)

            # if the difference is 1/2, then we have a palindrome
            if (len(all_letters_between) // 2) == len(unq_letters_between):

                # additional check
                # start from the center and expand outwards
                # left = center - 1
                # right = center + 1
                # count = 0
                # while left >= 0 and right < len(s) and all_letters_between[left] == all_letters_between[right]:
                #     left -= 1
                #     right += 1
                #     count += 1
                #
                # if count < len(all_letters_between) // 2:
                #     continue

                len_pal = all_len + 2
                if len_pal > max_pal:
                    max_pal = len_pal
                    largest_pal = letter + all_letters_between + letter

            if max_pal == len(s):
                return largest_pal

    return largest_pal


def get_largest_palindromic_2(s: str) -> str:
    """
    using Manacher's algorithm
    """
    # Make a new string with # between each letter
    # This is to handle even and odd length palindromes
    # 'aba' becomes '#a#b#a#' and 'abba' becomes '#a#b#b#a#'
    # Always creates an odd length string
    t = '#'.join(s)
    t = '#' + t + '#'

    # Initialize variables
    n = len(t)  # length of the modified string
    # this creates an array of 0's with length of n
    P = [0] * n  # will store the radius of the palindrome centered at each character
    # p will have values like: P[0],P[1],P[2],P[3],P[4] will be # 0,1,2,1,0
    # 0,1,2,1,0 respectively.
    C, R = 0, 0  # c=center, r=right boundary of the rightmost palindrome

    for i in range(n):
        # calculate the mirror index of i
        # i_mirror = C - (i - C)
        # handle odd and even length palindromes
        i_mirror = 2 * C - i

        # if i is within the right boundary R of the current palindrome, initialize P[i] based on the mirror index
        if i < R:
            P[i] = min(R - i, P[i_mirror])

        # This is where we find the palindrome and search left and right of the center
        # First test boundary conditions at left and right
        # Second test if left and right are equal, remember we have # between each letter and at beginning/end
        # #a#b#a#b#a#
        # expand around i
        # i = 0, left = -1, right = 1: so skip while loop
        # i = 1, left = 0, right = 2: enter while loop
        left = i - (1 + P[i])
        right = i + (1 + P[i])
        while left >= 0 and right < n and t[left] == t[right]:
            P[i] += 1
            left -= 1  # expand left
            right += 1  # expand right

        # if palindrome centered at i expands past R,
        # adjust center based on expanded palindrome.
        # adjust right boundary to the rightmost boundary of the palindrome
        if i + P[i] > R:
            C = i  # new center
            R = i + P[i]  # new right boundary, position of the rightmost character of the last palindrome

    # extract the longest palindrome
    maxlength = max(P)
    center_index = P.index(maxlength)
    return t[center_index - maxlength: center_index + maxlength + 1].replace('#', '')


if __name__ == '__main__':
    nums1 = [1, 2, 1]
    print(getConcatenation(nums1))

    s1 = "aabca"
    r = countPalindromicSubsequence(s1)
    print(r)
    print(get_palindromic_values(s1))

    s1 = "adc"
    r = countPalindromicSubsequence(s1)
    print(r)
    print(get_palindromic_values(s1))

    s1 = "bbcbaba"
    r = countPalindromicSubsequence(s1)
    print(r)
    print(get_palindromic_values(s1))

    # Get the largest palindromic
    print('********* Find the largest palindromic *********')
    s1 = "aacabdkacaa"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    # result should be "aca"
    # This test case fails, with the current logic
    # print(f"pal: ", get_largest_palindromic(s1))

    s1 = "babad"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = "babcddcbab"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = "a"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = "ac"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = "abb"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = 'abc'
    print(f'pal2: ', get_largest_palindromic_2(s1))
    # result should be "a"
    print(f'pal: ', get_largest_palindromic(s1))

    s1 = "abcdcba"
    print(f'pal2: ', get_largest_palindromic_2(s1))
    # result should be "abcdcba"
    print(f'pal: ', get_largest_palindromic(s1))


