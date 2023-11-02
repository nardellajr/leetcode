# 1431 Kids With the Greatest Number of Candies
# Difficulty: Easy
# return a list of boolean values representing whether each element of candies can be the greatest among n+k candies
# where n is the number of candies that the kid has and k is the extra candies that the kid can get

def kids_with_candies(candies, extra_candies):
    # set the maximum value testing variable, any candy that is greater than this value will be True
    max_candies = max(candies) - extra_candies
    return [candy >= max_candies for candy in candies]


if __name__ == '__main__':
    print(kids_with_candies([2, 3, 5, 1, 3], 3))
    print(kids_with_candies([4, 2, 1, 1, 2], 1))
    print(kids_with_candies([12, 1, 12], 10))
