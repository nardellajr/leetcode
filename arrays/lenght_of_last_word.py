# 58. Length of Last Word
# Easy
# Given a string s consists of some words separated by spaces,
# return the length of the last word in the string.


def length_of_last_word(s: str) -> int:
    # split string into array of words
    words = s.split()
    # if no words, return 0
    if len(words) == 0:
        return 0
    # return length of last word
    return len(words[-1])


if __name__ == '__main__':
    s = "Hello World"
    print(length_of_last_word(s))
    # should return 5

    s = "   fly me   to   the moon  "
    print(length_of_last_word(s))
    # should return 4

