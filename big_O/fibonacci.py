

def fib(n: int) -> int:
    if n < 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

# Time complexity:
# At each recursive call we are increasing the 2 fib calls by 1
# So, if the n = 4
# - First time 2 calls: 2**1
# - Second time 4 calls:  2**2
# - Third time, there could be 8 call, if some of the previous call didn't hit the termination logic:  2**3
# https://www.youtube.com/watch?v=CB8JPjg_3cM


if __name__ == '__main__':
    n = 20
    print(fib(n))
