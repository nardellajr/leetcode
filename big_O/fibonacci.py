

def fib(n: int) -> int:
    if n < 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

# Time complexity:
# At each recursive call we are doubling the number of fib calls
# So, if the n = 4
#
# - First time, n = 4, f(4) : 2**0
# - Second time f(3), f(2) :  2**1
# - Third time f(2) f(1)  f(1) f(0) : 2**2
# - Forth time, f(1) f(0),there could be 8 calls, if some of the previous call didn't hit the termination logic: 2**3
# https://www.youtube.com/watch?v=CB8JPjg_3cM

# This doubling of calls is equal to 2**n
# 2**0 + 2**1 + 2**2 + ... + 2**n-1
# 2**n  - 1 , but remember we drop the constant
# O(2**n) - Time Complexity


if __name__ == '__main__':
    n = 20
    print(fib(n))
