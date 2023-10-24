# 2355. Maximum Number of Books You Can Take

def maximumBooks(books: list[int]) -> int:
    n = len(books)

    # Helper function to calculate the sum of books in a given range [l, r]
    def calculateSum(l, r):
        # min between books[r] and the length of the contiguous section (r - 1 + 1)
        # imagine a section of the bookshelf l = 2 to r = 5 and books[r] (books[5]) is 4
        # cnt = min(4, 5 - 2 + 1) = min(4, 4) = 4
        # cnt is the actual number of books that can be taken from the last shelf in the contiguous section
        cnt = min(books[r], r - l + 1)

        # calculate the sum of the books in the contiguous section spanning from l to r
        # derived from the formula for the sum of an Arithmetic Sequence
        # if last shelf 4, second to last shelf 3, third to last shelf 2, first shelf 1:  1 + 2 + 3 + 4 = 10
        # equation =  (2 * 4 - (4 - 1)) * 4 // 2 = 10
        return (2 * books[r] - (cnt - 1)) * cnt // 2

    # initialized to keep track of the indices of the shelves you're considering
    # Purpose: keep track of indices that are "candidates" for forming a valid "CONTIGUOUS" sequence
    stack = []

    # each entry represent the maximum number of books that can be taken from the bookshelf up to index i
    # crucial for storing the best solutions to sub-problems
    dp = [0] * n

    for i in range(n):
        # While we cannot push i, we pop from the stack
        # stack is "truthy" when it's not empty, "falsy" when it's empty
        # first time through the loop, stack is empty, skip while loop
        # [8, 5, 2, 7, 9], "books[i] - i" , (8 - 0), then (5 - 1) is a score
        # algorithm keeps the stack in decreasing order of this "score" from bottom to top.
        # It believes that a higher "score" at a given point will more likely contribute to a larger contiguous
        # section in the future.
        while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
            stack.pop()

        # stack is empty ("falsy"), but "not" makes it True
        if not stack:
            dp[i] = calculateSum(0, i)
        else:
            j = stack[-1]
            dp[i] = dp[j] + calculateSum(j + 1, i)

        print(f"dp[{i}] = {dp[i]}")
        # Push the current index onto the stack
        stack.append(i)
        print(f"stack = {stack}\n")

    # Return the maximum element in the dp array
    return max(dp)


if __name__ == '__main__':
    # shelf_of_books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]
    # shelf_of_books = [7, 0, 3, 4, 5]
    shelf_of_books = [8, 5, 2, 7, 9]

    print(maximumBooks(shelf_of_books))
