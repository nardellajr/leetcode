# you are given an array of strings "words" and a character target
# return all the strings in "words" that contain the character "target"

# Example 1:
# words = ["leet", "code"], x = "e"
# output = [0, 1]
# Explanation: "e" occurs in both "leet" and "code", so we return [0, 1]


# Time: O(n) | Space: O(n)
def find_words_containing(words: list[str], x: str) -> list[int]:
    return [i for i, word in enumerate(words) if x in word]


# Time: O(n) | Space: O(n)
# Slower than the above solution
def find_words_containing2(words: list[str], x: str) -> list[int]:
    found_words = []
    counter = 0
    for w in words:
        try:
            if w.index(x) >= 0:
                found_words.append(counter)
            # if w.index(x):
            #    found_words.append(counter)
        except ValueError:
            pass
        counter += 1
    return found_words



if __name__ == '__main__':

    words = ["leet", "code"]
    x = "e"
    results = find_words_containing(words, x)
    print(results)

    results = find_words_containing2(words, x)
    print(results)

    words = ["abc","bcd","aaaa","cbc"]
    x = "a"
    results = find_words_containing(words, x)
    print(results)

    results = find_words_containing2(words, x)
    print(results)
