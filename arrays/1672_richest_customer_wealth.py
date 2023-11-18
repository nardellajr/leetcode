# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith
# customer has in the jth bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.
import time


def maximumWealth(accounts: list[list[int]]) -> int:
    # Brut force method

    richest = 0
    # number of customers
    for i in range(len(accounts)):
        # customers money in each bank
        total_money = 0
        for j in range(len(accounts[i])):
            # add money in each bank
            total_money += accounts[i][j]

        if total_money > richest:
            richest = total_money

    return richest


def maxWealth2(accounts: list[list[int]]) -> int:

    richest = 0
    for account in accounts:
        total_money = sum(account)

        if total_money > richest:
            richest = total_money

    return richest


def maxWealth3(accounts: list[list[int]]) -> int:
    return max(sum(account) for account in accounts)


if __name__ == '__main__':
    acc = [[1, 2, 3], [3, 2, 1]]
    begin = time.perf_counter()
    print(maximumWealth(acc))
    print(f"time: ", time.perf_counter() - begin)

    begin = time.perf_counter()
    print(maxWealth2(acc))
    print(f"time: ", time.perf_counter() - begin)

    begin = time.perf_counter()
    print(maxWealth3(acc))
    print(f"time: ", time.perf_counter() - begin)


    acc = [[1,5],[7,3],[3,5]]
    print(maximumWealth(acc))
    print(maxWealth2(acc))
    print(maxWealth3(acc))

    acc = [[2,8,7],[7,1,3],[1,9,5]]
    begin = time.perf_counter()
    print(maximumWealth(acc))
    print(f"time: ", time.perf_counter() - begin)

    begin = time.perf_counter()
    print(maxWealth2(acc))
    print(f"time: ", time.perf_counter() - begin)

    begin = time.perf_counter()
    print(maxWealth3(acc))
    print(f"time: ", time.perf_counter() - begin)


