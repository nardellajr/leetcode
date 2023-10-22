
# Problem Maximum Number of Books You Can Take from the Bookshelf
# while satisfying teh given conditions.
# For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.
# Return the maximum number of books you can take from the bookshelf


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
shelf_of_books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]
n = len(shelf_of_books)

# initialize DP table to all 0s
DP = [0] * n




