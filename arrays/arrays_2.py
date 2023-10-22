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



