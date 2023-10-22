
def merge_alternately_long(word1: str, word2: str) -> str:
    word3 = ''
    if len(word1) == len(word2):
        for x in range(len(word1)):
            word3 += word1[x] + word2[x]

        return word3
    elif len(word1) > len(word2):
        for x in range(len(word1)):
            if x >= len(word2):
                return word3 + word1[x:]
            else:
                word3 += word1[x] + word2[x]
    else:
        for x in range(len(word2)):
            if x >= len(word1):
                return word3 + word2[x:]
            else:
                word3 += word1[x] + word2[x]
    return word3

# merging to words together
def merge_alternately_short(word: str, word2: str) -> str:
   
    i = 0
    j = 0
    result = []
    
    w1 = len(word1)
    w2 = len(word2)
   
    # continue in loop while both pointers are less than the length of the words
    while i < w1 or j < w2:
        
        # test if i is less than the length of word1
        if i < w1:
            # add the letter to the result
            result += word1[i]
            i += 1
        
        # test if j is less than the length of word2
        if j < w2:
            # add the letter to the result
            result += word2[j]
            j += 1

    # return the result as a string
    return "".join(result)


if __name__ == '__main__':

    # Same size Case 1
    word1 = 'abc'
    word2 = 'pqr'
    merged = merge_alternately_long(word1, word2)
    print(f'Long Case 1', merged)
    merged2 = merge_alternately_short(word1, word2)
    print(f'Short Case 1', merged2)

    # Same size Case 2
    word1 = 'ab'
    word2 = 'pqrs'
    merged = merge_alternately_long(word1, word2)
    print(f'Case 2', merged)
    merged2 = merge_alternately_short(word1, word2)
    print(f'Short Case 2', merged2)

    # Same size Case 3
    word1 = 'abcd'
    word2 = 'pq'
    merged = merge_alternately_long(word1, word2)
    print(f'Case 3', merged)
    merged2 = merge_alternately_short(word1, word2)
    print(f'Short Case 3', merged2)


# for x in range(len(word1)):
#     print(word1[:x])

# gets the remaining strings
# print(word1[2:])


