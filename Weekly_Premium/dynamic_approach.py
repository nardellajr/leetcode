# This file contains a solution to the following LeetCode problem:
# Maximum Number of Books You Can Take from the Bookshelf
# while satisfying the given condition
# For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.
# Return the maximum number of books you can take from the bookshelf

# I thought my explanation above was correct, but after looking at the problem again, there is one constraint
# that I missed. "take books from a contiguous section of the bookshelf"

# ****** So the solution below IS NOT correct. *******


# Dynamic Programming (DP)
# define the Subproblem, the smallest subproblem that we can solve
# Create DP table, a data structure to hold the subproblem solutions
# Determine the relationship between the subproblems to fill in the DP table
# Base Case: identify the base case and fill them in the DP table
# Solve: Use the DP table to find the solution to the original problem

# Subproblem: the smallest subproblem that we can solve
# Given that we need to find the maximum number of books we can take under the constraints, our subproblem can be:

# Let DP[i] represent the maximum number of books that can be taken from the bookshelf
# starting from index 0 to index i under the given constraints.

# By solving smaller instances of this subproblem, we can build up to the solution for the entire array
# DP[n - 1], where n is the length of the array.


# Create DP table, a data structure to hold the subproblem solutions
# array of length n, where n is the number of shelves. Each DP[i] will hold the maximum number of books
# that can be taken from the bookshelf starting from index 0 to index i under the given constraints.
# shelf_of_books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]
# shelf_of_books = [7, 0, 3, 4, 5]
shelf_of_books = [8, 5, 2, 7, 9]
n = len(shelf_of_books)

# initialize DP table to all 0s
DP = [0] * n

for i in range(n):
    DP[i] = shelf_of_books[i]
    for j in range(i):
        if shelf_of_books[j] < shelf_of_books[i]:
            DP[i] = max(DP[i], DP[j] + shelf_of_books[i])

final_answer = max(DP)
print(DP)
print(final_answer)




