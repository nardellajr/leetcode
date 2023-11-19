# 2114. Maximum number of words found in sentences

# A sentence is a list of works that are separated by a single space with no leading or trailing spaces
# You are given an array of strings sentences, where each sentences[i] represents a single sentence
# Return the maximum number of words that appear in a single sentence

import time


def mostWordsFound(sentences: list[str]) -> int:
    """
    Brute force
    """
    max_sentence_count = 0
    for s in sentences:
        # verify no leading or trailing space
        if s[0] == ' ' or s[:0] == ' ':
            continue

        space_count = 0
        for space in s:
            if space == ' ':
                space_count += 1

        space_count += 1 # Add 1 to account for the words
        if space_count > max_sentence_count:
            max_sentence_count = space_count

    return max_sentence_count


# Time O(n*m), where n = sentences, m = average length of a sentence
def mostWordsFound1(sentences: list[str]) -> int:
    return max(s.count(' ') for s in sentences) + 1


if __name__ == '__main__':

    sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
    begin_time = time.perf_counter()
    c = mostWordsFound(sentences)
    print('Total time: ', time.perf_counter() - begin_time)
    print(f'Maximum Words Found: {c}')


    begin_time = time.perf_counter()
    c = mostWordsFound1(sentences)
    print('Total time: ', time.perf_counter() - begin_time)
    print(f'Maximum Words Found: {c}')



