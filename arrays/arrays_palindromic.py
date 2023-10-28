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
    unique_str = set(s)
    largest_pal = ""
    max_pal = 0
    if len(unique_str) == 1:
        return s
    elif len(unique_str) == len(s) and len(unique_str) == 2:
        return s[0]

    for letter in unique_str:
        start = s.find(letter)
        end = s.rfind(letter)

        if start < end:
            all_letters_between = s[start + 1: end]
            unq_letters_between = set(s[start + 1: end])
            # if the difference is 1/2, then we have a palindrome
            if ((len(all_letters_between) / 2) == len(unq_letters_between)) or (len(all_letters_between) == 1):
                len_pal = len(all_letters_between) + 2
                if len_pal > max_pal:
                    max_pal = len_pal
                    largest_pal = letter + all_letters_between + letter

    return largest_pal


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
    s1 = "babad"
    print(get_largest_palindromic(s1))

    s1 = "babcddcbad"
    print(get_largest_palindromic(s1))

    s1 = "a"
    print(get_largest_palindromic(s1))

    s1 = "ac"
    print(get_largest_palindromic(s1))

    s1 = "abb"
    print(get_largest_palindromic(s1))

    s1 = "abcba"
    print(get_largest_palindromic(s1))
    # result should be "abcba"
